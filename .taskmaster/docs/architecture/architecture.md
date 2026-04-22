# System Architecture: DBSN Centralized Digital Ecosystem

## 1. Architecture Overview

### Core Tech Stack Summary

- **Application Runtime:** Next.js 14+ (App Router, Route Handlers, Server Components where applicable)
- **Repository Strategy:** Turborepo monorepo with shared packages for UI, config, and utilities
- **Content Layer:** Sanity.io (headless CMS, schema-driven content federation)
- **UI System:** Tailwind CSS + Radix UI (shared tokenized design system)
- **Transactional Data Layer:** PlanetScale (MySQL-compatible)
- **Authentication:** NextAuth.js (role-based access: `admin`, `viewer`, `client`)
- **Hosting / Edge:** Cloudflare Pages (+ Cloudflare edge redirect handling)
- **Notifications:** Resend (email), Telegram Bot API (internal ops alerting)
- **Telemetry:** GA4 + GSC + Cloudflare Analytics
- **Messaging Fallback:** WhatsApp `wa.me` pre-filled fallback for RFQ failure path

### High-Level System Topology (Hub-and-Spoke)

```mermaid
flowchart TD
    U["Users\nB2G Procurement / B2B Technical Buyers / Internal Admin"]

    subgraph DNS["Public Domains"]
        HUB["sentradaya.com\nHub (Corporate Trust Center)"]
        PJU["pju.sentradaya.com\nProduct Spoke"]
        SOL["solarcell.sentradaya.com\nProduct Spoke"]
        LGT["alatpetir.sentradaya.com\nProduct Spoke"]
        BAT["baterai.sentradaya.com\nProduct Spoke (Extensible)"]
        DASH["dashboard.sentradaya.com\nSecure Tracking Portal"]
    end

    subgraph EDGE["Cloudflare Edge"]
        CF["Cloudflare Pages\nCDN + TLS + Hosting"]
        REDIR["Redirect Resolver\n(redirect_map-driven 301)"]
    end

    subgraph APP["Next.js 14 Monorepo (Turborepo)"]
        WEB["Hub + Spokes Web App\n(App Router)"]
        API["Route Handlers\n/api/rfq, /api/tracking, /api/admin/*"]
        AUTH["NextAuth.js\nSession + RBAC"]
        UI["Shared UI Package\nTailwind + Radix"]
    end

    subgraph DATA["Data & Integrations"]
        SANITY["Sanity CMS\nProduct/Certification/Portfolio/Page/SpokeConfig"]
        PS["PlanetScale\nleads, users, redirect_map"]
        RESEND["Resend Email API"]
        TG["Telegram Bot API"]
        GA["GA4 + GSC + Cloudflare Analytics"]
        WA["WhatsApp wa.me Fallback"]
    end

    subgraph LEGACY["Legacy Domains"]
        L1["pjusolarcellindonesia.com"]
        L2["sentradaya.com (legacy)"]
        L3["alatpenangkalpetir.co.id"]
    end

    U --> HUB
    U --> PJU
    U --> SOL
    U --> LGT
    U --> BAT
    U --> DASH

    HUB --> CF
    PJU --> CF
    SOL --> CF
    LGT --> CF
    BAT --> CF
    DASH --> CF

    L1 --> REDIR
    L2 --> REDIR
    L3 --> REDIR
    REDIR --> CF

    CF --> WEB
    WEB --> UI
    WEB --> SANITY
    WEB --> API
    API --> PS
    API --> RESEND
    API --> TG
    API --> AUTH
    AUTH --> PS
    WEB --> GA
    API --> WA
```

## 2. Component Breakdown

### Frontend

- **Runtime + Routing:** Next.js 14 App Router; route segmentation by host/subdomain and route groups.
- **Domain Surfaces:**
  - Hub: corporate trust center (`sentradaya.com`)
  - Product spokes: product content + RFQ entry (`pju`, `solarcell`, `alatpetir`, `baterai`)
  - Dashboard spoke: authenticated client tracking (`dashboard.sentradaya.com`)
- **UI Architecture:**
  - Shared component package in monorepo (`@dbsn/ui` equivalent)
  - Shared Tailwind token config at repo root (no spoke-local divergence)
  - Shared primitives: navigation, trust badges, certification cards, product spec tables, RFQ form shells, auth forms, tracking status cards
- **Rendering Strategy:**
  - CMS-driven static/ISR where content is stable (hub/spokes content pages)
  - Server-side protected render for dashboard tracking views
- **Mobile-first enforcement:**
  - RFQ and login forms with minimum 44px touch targets
  - Floating WhatsApp CTA collision prevention on form pages

### Backend

- **Edge-facing app backend:** Next.js Route Handlers under `/api/*`.
- **Core service domains:**
  1. RFQ ingestion (validation, persistence, notification, fallback orchestration)
  2. Authentication/session issuance (NextAuth)
  3. Admin lead operations (query/filter/update lifecycle)
  4. Client tracking retrieval (authorized status read by `tracking_scope_ids` / `linked_lead_id`)
- **Validation controls:**
  - Server-side input sanitization
  - Anti-spam controls (honeypot + rate limiting)
  - Strict 4xx/5xx response semantics
- **Authorization model:**
  - `admin`/`viewer`: internal dashboard access
  - `client`: dashboard tracking access only
  - Ownership guard: client can read only rows bound to their lead/tracking scope

### Infrastructure/DevOps

- **Hosting:** Cloudflare Pages for all domains/subdomains.
- **Routing model:** Hostname-based routing into one monorepo deployment target.
- **Redirect engine:**
  - Data source: PlanetScale `redirect_map`
  - Resolution order: exact match → pattern match → parent category fallback → spoke home → hub home
  - Hard rule: no unresolved legacy 404 during migration window
- **Database:** PlanetScale MySQL-compatible, TLS-enforced connections, least-privilege credentials.
- **Operational integrations:** Resend + Telegram for RFQ and failure alerting; optional client access lifecycle alerts.
- **Telemetry pipeline:** event instrumentation to GA4, search visibility via GSC, infra analytics via Cloudflare.

## 3. Data Architecture & Schema

### Entity-Relationship Diagram (CMS + Transactional)

```mermaid
erDiagram
    SPOKE_CONFIG ||--o{ PRODUCT : "featuredProducts"
    SPOKE_CONFIG ||--o{ PAGE : "targetSpoke"
    SPOKE_CONFIG ||--o{ PORTFOLIO_ENTRY : "relatedSpoke"

    PRODUCT }o--o{ CERTIFICATION : "relatedCertifications"
    PORTFOLIO_ENTRY }o--o{ PRODUCT : "relatedProducts"

    LEADS ||--o| USERS : "linked_lead_id"

    SPOKE_CONFIG {
      string id PK
      string name
      string subdomain
      string tagline
      string heroImage
      string primaryColor
      json featuredProducts
      json seoDefaults
    }

    PRODUCT {
      string id PK
      string title
      string slug
      string spoke_ref FK
      string shortDescription
      text fullDescription
      json specifications
      json images
      string datasheetFile
      json relatedCertifications
      json seoMeta
    }

    CERTIFICATION {
      string id PK
      string title
      string slug
      string certificationBody
      enum certType
      date issueDate
      date expiryDate
      string documentFile
      string coverImage
      boolean isIndexable
      json seoMeta
    }

    PORTFOLIO_ENTRY {
      string id PK
      string title
      string slug
      string projectType
      enum clientCategory
      string location
      int completionYear
      text scopeDescription
      string outcome
      json images
      string relatedSpoke FK
      json relatedProducts
    }

    PAGE {
      string id PK
      string title
      string slug
      string targetSpoke FK_nullable
      json sections
      json seoMeta
    }

    LEADS {
      string id PK
      datetime created_at
      datetime updated_at
      enum segment
      string source_domain
      string source_page_path
      string source_campaign_tag
      string utm_source
      string utm_medium
      string utm_campaign
      string contact_name
      string contact_email
      string contact_phone
      string company_name
      string product_category
      int quantity
      text project_scope
      string timeline
      string procurement_type_nullable
      text notes
      enum submission_status
      boolean fallback_triggered
      text fallback_wa_url_nullable
      string tracking_project_id_nullable
      datetime dashboard_access_granted_at_nullable
      enum dashboard_access_status
    }

    USERS {
      string id PK
      string email
      string name
      enum role
      datetime created_at
      string linked_lead_id FK_nullable
      string client_company_name_nullable
      enum tracking_scope_type_nullable
      json tracking_scope_ids_nullable
      datetime last_login_at_nullable
      boolean is_active
    }

    REDIRECT_MAP {
      string legacy_url PK
      string target_url
      string spoke
    }
```

### Detailed Schema Definitions

#### Sanity CMS Schemas

1. **Product**
   - `title: string`
   - `slug: slug`
   - `spoke: reference(SpokeConfig)`
   - `shortDescription: string`
   - `fullDescription: portableText`
   - `specifications: array<{ key: string; value: string }>`
   - `images: array<image>`
   - `datasheetFile: file`
   - `relatedCertifications: array<reference(Certification)>`
   - `seoMeta: { title: string; description: string; ogImage: image }`

2. **Certification**
   - `title: string`
   - `slug: slug`
   - `certificationBody: string`
   - `certType: enum('SNI'|'TKDN'|'LKPP'|'ISO'|'Other')`
   - `issueDate: date`
   - `expiryDate: date`
   - `documentFile: file`
   - `coverImage: image`
   - `isIndexable: boolean`
   - `seoMeta: object`

3. **PortfolioEntry**
   - `title: string`
   - `slug: slug`
   - `projectType: string`
   - `clientCategory: enum('Government'|'BUMN'|'Private'|'EPC')`
   - `location: string`
   - `completionYear: number`
   - `scopeDescription: portableText`
   - `outcome: string`
   - `images: array<image>`
   - `relatedSpoke: reference(SpokeConfig)`
   - `relatedProducts: array<reference(Product)>`

4. **SpokeConfig**
   - `name: string`
   - `subdomain: string`
   - `tagline: string`
   - `heroImage: image`
   - `primaryColor: string (design token)`
   - `featuredProducts: array<reference(Product)>`
   - `seoDefaults: object`

5. **Page**
   - `title: string`
   - `slug: slug`
   - `targetSpoke: reference(SpokeConfig) | null`
   - `sections: array<portableText|customBlock>`
   - `seoMeta: object`

#### PlanetScale Transactional Schemas (MySQL-Compatible)

1. **`leads`**
   - `id CHAR(36) PRIMARY KEY` (CUID storage)
   - `created_at DATETIME NOT NULL`
   - `updated_at DATETIME NOT NULL`
   - `segment ENUM('B2G','B2B') NOT NULL`
   - `source_domain VARCHAR(255) NOT NULL`
   - `source_page_path VARCHAR(512) NOT NULL`
   - `source_campaign_tag VARCHAR(255) NULL`
   - `utm_source VARCHAR(255) NULL`
   - `utm_medium VARCHAR(255) NULL`
   - `utm_campaign VARCHAR(255) NULL`
   - `contact_name VARCHAR(255) NOT NULL`
   - `contact_email VARCHAR(255) NOT NULL`
   - `contact_phone VARCHAR(50) NOT NULL`
   - `company_name VARCHAR(255) NOT NULL`
   - `product_category VARCHAR(255) NOT NULL`
   - `quantity INT NULL`
   - `project_scope TEXT NULL`
   - `timeline VARCHAR(255) NULL`
   - `procurement_type VARCHAR(255) NULL` (B2G only)
   - `notes TEXT NULL`
   - `submission_status ENUM('received','contacted','qualified','disqualified') NOT NULL DEFAULT 'received'`
   - `fallback_triggered BOOLEAN NOT NULL DEFAULT FALSE`
   - `fallback_wa_url TEXT NULL`
   - `tracking_project_id VARCHAR(255) NULL`
   - `dashboard_access_granted_at DATETIME NULL`
   - `dashboard_access_status ENUM('not_eligible','pending','granted','revoked') NOT NULL DEFAULT 'not_eligible'`

2. **`users`**
   - `id CHAR(36) PRIMARY KEY`
   - `email VARCHAR(255) UNIQUE NOT NULL`
   - `name VARCHAR(255) NOT NULL`
   - `role ENUM('admin','viewer','client') NOT NULL`
   - `created_at DATETIME NOT NULL`
   - `linked_lead_id CHAR(36) NULL` (FK to `leads.id`, nullable)
   - `client_company_name VARCHAR(255) NULL`
   - `tracking_scope_type ENUM('project','order') NULL`
   - `tracking_scope_ids JSON NULL`
   - `last_login_at DATETIME NULL`
   - `is_active BOOLEAN NOT NULL DEFAULT TRUE`

3. **`redirect_map`**
   - `legacy_url VARCHAR(1024) PRIMARY KEY`
   - `target_url VARCHAR(1024) NOT NULL`
   - `spoke VARCHAR(100) NOT NULL`

## 4. API & Integration Strategy

### Internal API Endpoints

1. `POST /api/rfq`
   - Purpose: ingest segmented RFQ (`B2G`/`B2B`)
   - Input: validated form payload + source attribution + UTM
   - Writes: `leads`
   - Side-effects: Resend ACK + internal email, Telegram alert
   - Failure behavior: returns `500|timeout` and provides fallback contract for WhatsApp pre-fill

2. `GET|POST /api/auth/[...nextauth]`
   - Purpose: NextAuth session lifecycle
   - Roles: `admin`, `viewer`, `client`
   - Enforces protected route access and session integrity

3. `GET /api/dashboard/tracking`
   - Auth: required, `role=client`
   - Input: implied from authenticated user (`linked_lead_id`, `tracking_scope_ids`)
   - Output: authorized project/order tracking statuses only
   - Deny behavior: `401` (unauthenticated), `403` (scope violation), logged event

4. `GET /api/admin/leads`
   - Auth: required, `role in ('admin','viewer')`
   - Supports: search/filter by segment/source/submission status

5. `PATCH /api/admin/leads/:id/status`
   - Auth: required, `role=admin`
   - Updates: `submission_status`, `dashboard_access_status`, `dashboard_access_granted_at`, `tracking_project_id`
   - Optional side-effects: provisioning email + Telegram audit message

### Third-Party Integrations

1. **Resend**
   - Trigger A: successful RFQ submit → customer ACK email
   - Trigger B: successful RFQ submit → internal notification email
   - Trigger C: dashboard access grant → provisioning email with secure login/reset path

2. **Telegram Bot API**
   - Trigger A: RFQ success notification to sales ops channel
   - Trigger B: RFQ failure/fallback trigger alert
   - Trigger C (optional per PRD): client access provisioning/revocation audit alerts

3. **WhatsApp (wa.me fallback)**
   - Trigger: RFQ API/database failure
   - Mechanism: serialized captured RFQ payload into pre-filled URL parameters
   - UX requirement: explicit failure messaging and primary fallback CTA

## 5. Key Architectural Flows

### RFQ Submission + Fallback Flow

```mermaid
sequenceDiagram
    actor User
    participant UI as Spoke RFQ Form (Next.js)
    participant API as POST /api/rfq
    participant DB as PlanetScale (leads)
    participant Resend as Resend API
    participant TG as Telegram Bot API
    participant WA as WhatsApp wa.me
    participant GA as GA4

    User->>UI: Fill RFQ fields (B2G/B2B)
    UI->>GA: rfq_start
    User->>UI: Submit form
    UI->>GA: rfq_submit_attempt
    UI->>API: JSON payload + attribution + UTM

    alt Valid + DB available
        API->>API: Validate, sanitize, anti-spam checks
        API->>DB: INSERT leads row
        DB-->>API: lead_id
        API->>Resend: ACK email + internal email
        API->>TG: New RFQ alert
        API-->>UI: 200 {success:true, lead_id}
        UI->>GA: rfq_submit_success
        UI-->>User: Confirmation state
    else Validation failure
        API-->>UI: 422 {field_errors}
        UI-->>User: Inline correction prompts
    else Infrastructure failure
        API-->>UI: 500/timeout
        UI->>GA: rfq_submit_failure {fallback_triggered:true}
        UI->>WA: Build pre-filled wa.me URL
        UI-->>User: Fallback prompt + primary WhatsApp CTA
        User->>WA: Open WhatsApp handoff
        UI->>GA: whatsapp_click {cta_location:"fallback"}
        API->>TG: Failure alert
    end
```

### Authentication + Tracking Dashboard Flow

```mermaid
sequenceDiagram
    actor Client as B2B/B2G Client User
    participant Dash as dashboard.sentradaya.com
    participant Auth as NextAuth.js
    participant DB as PlanetScale (users, leads)
    participant TrackAPI as GET /api/dashboard/tracking
    participant GA as GA4

    Client->>Dash: Open login page
    Client->>Auth: Submit credentials
    Auth->>DB: Lookup user by email

    alt Active client account + valid credentials
        DB-->>Auth: user(role=client, linked_lead_id, tracking_scope_ids, is_active=true)
        Auth->>DB: Update last_login_at
        Auth-->>Dash: Issue authenticated session
        Dash->>GA: dashboard_login_success
        Dash->>TrackAPI: Request tracking data (session-bound)
        TrackAPI->>DB: Resolve lead + authorized tracking scopes
        DB-->>TrackAPI: Tracking status rows
        TrackAPI-->>Dash: 200 authorized tracking payload
        Dash->>GA: tracking_status_view
        Dash-->>Client: Render project/order status
    else Invalid credentials or inactive/revoked account
        Auth-->>Dash: 401/403
        Dash->>GA: dashboard_login_failure
        Dash-->>Client: Access denied message
    else Authenticated but scope violation
        TrackAPI-->>Dash: 403 forbidden
        Dash-->>Client: Unauthorized tracking scope
    end
```

## 6. Technical Constraints & Security

1. **Authentication (AuthN):**
   - NextAuth.js mandatory for all protected surfaces.
   - Dashboard routes must reject unauthenticated requests with `401`.

2. **Authorization (AuthZ):**
   - Role model fixed: `admin`, `viewer`, `client`.
   - Client tracking endpoint must enforce ownership checks using `linked_lead_id` + `tracking_scope_ids`.
   - Scope violations must return `403` and be auditable.

3. **Input Security + Anti-Abuse:**
   - RFQ endpoint requires server-side sanitization, honeypot, and rate limiting.
   - No trust in client-submitted role/segment flags without server validation.

4. **Data Security:**
   - TLS-only DB transport.
   - Principle of least privilege for DB credentials and API keys.
   - No PII in GA4 or Cloudflare raw telemetry payloads.

5. **Operational Resilience:**
   - RFQ fallback to WhatsApp is mandatory on API/DB failure.
   - Telegram failure alerts are mandatory in fallback scenarios.

6. **Performance Constraints:**
   - Mobile PSI target: **>= 90** on hub, spoke, RFQ, dashboard login, tracking pages.
   - TTFB target: sub-second via Cloudflare edge.
   - Core Web Vitals must pass acceptable thresholds (LCP, INP/FID, CLS).
   - `next/image` mandatory for image optimization.

7. **Routing/SEO Constraints:**
   - Legacy URL migration must never terminate in unresolved 404 during migration window.
   - Canonical tags required on all authority pages.

## 7. AI Implementation Handoff (Build Order)

1. **Initialize Monorepo Foundations**
   1.1 Configure Turborepo workspaces and shared packages (`ui`, `config`, `types`).
   1.2 Scaffold Next.js 14 app structure with App Router and host-aware routing utilities.
   1.3 Implement shared Tailwind + Radix baseline tokens at root.

2. **Implement Domain Routing + Edge Topology**
   2.1 Bind hub and spoke hostnames to Cloudflare Pages.
   2.2 Implement hostname resolution middleware/utilities for hub, product spokes, and dashboard spoke.
   2.3 Add legacy redirect resolver integration contract (backed by `redirect_map`).

3. **Build CMS Contracts**
   3.1 Define Sanity schemas: `Product`, `Certification`, `PortfolioEntry`, `SpokeConfig`, `Page`.
   3.2 Implement GROQ query layer for spoke-aware data retrieval.
   3.3 Validate spoke rendering is data-driven with zero code forks.

4. **Provision Transactional Data Layer**
   4.1 Create PlanetScale schema: `leads`, `users`, `redirect_map` exactly per PRD v3 fields.
   4.2 Add indexes for lead lifecycle filters, source attribution, and linked client lookup.
   4.3 Add migration validation for enum coverage and nullable constraints.

5. **Implement Authentication + Authorization**
   5.1 Integrate NextAuth route handlers.
   5.2 Implement role model (`admin`, `viewer`, `client`) and route guards.
   5.3 Enforce client row-level tracking authorization via `linked_lead_id` + `tracking_scope_ids`.

6. **Implement RFQ Pipeline**
   6.1 Build segmented RFQ API (`/api/rfq`) with strict server-side validation.
   6.2 Persist leads with source attribution + UTM.
   6.3 Implement deterministic success/failure response contracts.

7. **Implement Notification Integrations**
   7.1 Wire Resend for ACK + internal lead email templates.
   7.2 Wire Telegram alerts for RFQ success and fallback failures.
   7.3 Implement dashboard provisioning notification on access grant.

8. **Implement WhatsApp Fallback Engine**
   8.1 Serialize captured RFQ fields to wa.me prefill format.
   8.2 Render explicit fallback UI and elevated primary CTA.
   8.3 Emit fallback telemetry (`rfq_submit_failure`, fallback `whatsapp_click`).

9. **Implement Admin Dashboard**
   9.1 Build protected lead listing with filter/search/source tags.
   9.2 Implement lifecycle updates (`submission_status`, `dashboard_access_status`, `tracking_project_id`).
   9.3 Add export-ready query/model structure.

10. **Implement Client Tracking Dashboard (`dashboard.sentradaya.com`)**
    10.1 Build login + session-protected routes.
    10.2 Build tracking status API bound to authorized scope.
    10.3 Build tracking UI cards/list with mobile-first behavior.

11. **Instrumentation + Telemetry Completion**
    11.1 Implement mandatory GA4 events from PRD (RFQ, WhatsApp, file, hub-spoke, dashboard login, tracking view).
    11.2 Validate no PII leakage in event payloads.
    11.3 Integrate Cloudflare + GSC verification.

12. **Quality Gates and Release Validation**
    12.1 Execute forced RFQ failure test and verify fallback + Telegram alert.
    12.2 Execute dashboard access/data-isolation tests (including forbidden cross-account access).
    12.3 Validate subdomain routing, redirect coverage, CWV/PSI thresholds, and launch gate checklist.
