# PRD: DBSN Unified Digital Ecosystem (Hub-and-Spoke Sub-domain Architecture)

**Author:** Pramono
**Date:** 2026-04-20
**Status:** Draft (Discovery Complete)
**Version:** 1.0
**Taskmaster Optimized:** Yes

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Problem Statement](#problem-statement)
3. [Goals & Success Metrics](#goals--success-metrics)
4. [User Stories](#user-stories)
5. [Functional Requirements](#functional-requirements)
6. [Non-Functional Requirements](#non-functional-requirements)
7. [Technical Considerations](#technical-considerations)
8. [Implementation Roadmap](#implementation-roadmap)
9. [Out of Scope](#out-of-scope)
10. [Open Questions & Risks](#open-questions--risks)
11. [Validation Checkpoints](#validation-checkpoints)
12. [Appendix: Task Breakdown Hints](#appendix-task-breakdown-hints)

---

## Executive Summary

DBSN currently operates three separate websites that built valuable SEO coverage but now create trust fragmentation, weak conversion flow, and operational overhead. This project introduces a **Greenfield** unified digital ecosystem using a **Hub-and-Spoke sub-domain architecture**: one corporate trust hub plus product-focused sub-domains with a shared design system and centralized lead/RFQ pipeline. The expected impact is preserved SEO equity during migration, higher qualified B2B/B2G conversion, stronger procurement trust signals, and better operational control through one maintainable platform.

---

## Problem Statement

### Current Situation
DBSN’s digital presence is split across:
- `pjusolarcellindonesia.com`
- `sentradaya.com`
- `alatpenangkalpetir.co.id`

This structure helped keyword-level visibility but now causes fragmented branding, inconsistent UX, and duplicated content operations.

### User Impact
- **Who is affected:**
  - Government Procurement Officers (PPK, Pengadaan staff, BUMN procurement)
  - B2B private buyers (procurement managers, EPC/project engineers, facility managers)
- **How they are affected:**
  - Trust friction from inconsistent brand footprints
  - Limited self-service procurement support (certifications, structured docs, RFQ)
  - Conversion friction from WhatsApp-only dominant path
- **Severity:** High (direct effect on qualification and vendor confidence)

### Business Impact
- **Cost of problem:** lost qualified leads due to early funnel drop-off and trust gaps.
- **Opportunity cost:** inability to fully monetize accumulated SEO and multi-vertical positioning.
- **Strategic importance:** critical for DBSN’s institutional positioning in B2G/B2B infrastructure projects.

### Why Solve This Now?
- DBSN has outgrown a multi-site operational model.
- SEO migration risk is highest if not planned as a structured initiative.
- Competition is increasing in renewable/electrical B2B digital channels.
- Internal strategic directive explicitly prioritizes trust signals and conversion architecture.

---

## Goals & Success Metrics

### Goal 1: Preserve and Consolidate SEO Equity
- **Description:** Maintain legacy organic strength while migrating to new architecture.
- **Metric:** Post-migration organic traffic retention.
- **Baseline:** Combined pre-migration organic traffic from 3 domains.
- **Target:** ≥70% retained within 6 months of launch.
- **Timeframe:** Month 1 to Month 6 post-launch.
- **Measurement Method:** Google Search Console + GA4 + Cloudflare Analytics.

### Goal 2: Increase Qualified Conversion
- **Description:** Improve structured lead capture quality and volume.
- **Metric:** Qualified RFQ submissions/month.
- **Baseline:** Current WhatsApp-led inquiry baseline.
- **Target:** Significant month-over-month uplift post-launch (tracked by segment).
- **Timeframe:** First 3 months post-launch.
- **Measurement Method:** Centralized dashboard with source attribution.

### Goal 3: Improve Procurement Trust Engagement
- **Description:** Increase interaction with compliance and technical documentation.
- **Metric:** Certification and datasheet download rate.
- **Baseline:** Low/fragmented current document access.
- **Target:** Continuous growth trend within first quarter post-launch.
- **Timeframe:** Month 1–3 post-launch.
- **Measurement Method:** File event tracking in GA4 + CMS analytics.

### Goal 4: Improve Conversion Efficiency by Entry Context
- **Description:** Improve product-page-to-inquiry funnel quality.
- **Metric:** Product page engagement to RFQ/WhatsApp conversion rate.
- **Baseline:** Current conversion path mostly WhatsApp-only.
- **Target:** Measurable lift on each spoke.
- **Timeframe:** First 90 days.
- **Measurement Method:** GA4 funnel events + CRM conversion tagging.

### Goal 5: Ensure Lead Operations Unification
- **Description:** Remove lead silos across hub/spokes.
- **Metric:** Lead centralization completeness.
- **Baseline:** Fragmented inbound across legacy sites.
- **Target:** 100% of leads/RFQs captured in centralized dashboard with source tags.
- **Timeframe:** At launch.
- **Measurement Method:** Dashboard audit and reconciliation.

### Goal 6: Capture Government Procurement Fit
- **Description:** Validate the platform can attract qualified B2G interest.
- **Metric:** LKPP-Qualified Inquiry Rate.
- **Baseline:** Not explicitly tracked today.
- **Target:** Establish and grow a stable qualified baseline.
- **Timeframe:** Month 1–3 post-launch.
- **Measurement Method:** RFQ form qualifiers + internal sales validation.

### Goal 7: Mobile-First Performance Excellence
- **Description:** Maintain strong mobile experience in Indonesia’s mobile-dominant usage context.
- **Metric:** PageSpeed Insights mobile score.
- **Baseline:** To be benchmarked in Sprint 1.
- **Target:** 90+ on key templates across hub and spokes.
- **Timeframe:** By launch and maintained post-launch.
- **Measurement Method:** PSI + Lighthouse CI.

### Goal 8: Optimize Hub-to-Spoke Journey Flow
- **Description:** Ensure the hub effectively routes users to relevant product spokes.
- **Metric:** Hub-to-Spoke CTR and journey completion flow.
- **Baseline:** N/A (new architecture).
- **Target:** Strong routing efficiency by key segment paths.
- **Timeframe:** Month 1–2 post-launch.
- **Measurement Method:** GA4 pathing + event instrumentation.

---

## User Stories

### Story 1: Government Procurement Validation Journey
**As a** Government Procurement Officer,
**I want to** validate DBSN certifications, references, and capability before contact,
**So that I can** shortlist DBSN as a compliant, credible vendor.

**Acceptance Criteria:**
- [ ] I can access SNI/TKDN/LKPP-related documents from the hub.
- [ ] I can view structured project references relevant to public infrastructure.
- [ ] I can submit a government-labeled RFQ with procurement details.
- [ ] Mobile CTA does not obstruct form interaction.
- [ ] If RFQ fails technically, I get fallback pre-filled WhatsApp flow.

**Task Breakdown Hint:**
- Build certifications hub content model + pages (~8h)
- Build government RFQ variant + validation (~10h)
- Add failure fallback to WhatsApp (~4h)

**Dependencies:** REQ-001, REQ-003, REQ-006

---

### Story 2: B2B Technical Buyer Self-Service Journey
**As a** B2B private-sector procurement/engineering user,
**I want to** compare offerings and access technical docs quickly,
**So that I can** make a faster, lower-friction shortlisting decision.

**Acceptance Criteria:**
- [ ] Product spoke pages include clear specifications and request-price path.
- [ ] Datasheets are downloadable without mandatory sign-up (Phase 1).
- [ ] RFQ captures project scope and timeline details.
- [ ] WhatsApp click-to-chat remains available and tracked.
- [ ] Page performance remains mobile-optimized.

**Task Breakdown Hint:**
- Build spoke product templates + Sanity schema (~12h)
- Build docs library + assets delivery strategy (~8h)
- Add event tracking for RFQ vs WhatsApp (~4h)

**Dependencies:** REQ-002, REQ-004, REQ-005, REQ-008

---

### Story 3: Internal Sales/Ops Unified Lead Management
**As an** internal DBSN sales/admin operator,
**I want to** manage all leads and RFQs from one dashboard,
**So that I can** prioritize follow-up and track performance by source.

**Acceptance Criteria:**
- [ ] All hub/spoke RFQs are written to one transactional DB.
- [ ] Lead records include source domain/page/campaign tags.
- [ ] Email + Telegram alerts trigger for new RFQs.
- [ ] Access is authenticated and role-controlled.
- [ ] Dashboard supports filtering by segment (Government vs Private).

**Task Breakdown Hint:**
- Build shared lead ingestion API + schema (~10h)
- Build dashboard list/filter views (~12h)
- Integrate alerting and auth (~8h)

**Dependencies:** REQ-007, REQ-009, REQ-010

---

## Functional Requirements

### Must Have (P0) - Critical for Launch

#### REQ-001: Main Hub (Root Domain) Trust Platform
**Description:** Implement root-domain hub for corporate profile, legal/certification trust assets, cross-sector portfolio, and navigation to product spokes.

**Acceptance Criteria:**
- [ ] Hub includes company profile, legal credibility content, and strategic CTAs.
- [ ] Hub links to all active spokes with consistent UX.
- [ ] Certifications section supports downloadable files.
- [ ] Portfolio section is first-class navigation.

**Task Breakdown:**
- Hub IA + page templates: Medium (6-8h)
- Certification/portfolio components: Medium (6-8h)
- QA + content checks: Small (3-4h)

**Dependencies:** Sanity schema readiness.

#### REQ-002: Product Spoke Sub-domains
**Description:** Each product cluster must run on dedicated sub-domain with shared codebase/templates and distinct product content.

**Acceptance Criteria:**
- [ ] Sub-domain routing is operational for each spoke.
- [ ] Shared design system used identically across spokes.
- [ ] Content differences are data-driven (not divergent code forks).

**Dependencies:** Monorepo foundation, routing strategy.

#### REQ-003: Certifications Hub
**Description:** Deliver centralized certifications/document trust center (SNI, TKDN, supporting legal/proof artifacts).

**Acceptance Criteria:**
- [ ] Structured metadata for each document.
- [ ] Download access works on mobile and desktop.
- [ ] Document pages are indexable where appropriate.

**Dependencies:** Sanity content model + CDN delivery.

#### REQ-004: Structured RFQ System (Segmented)
**Description:** Build RFQ forms for Government and Private pathways with structured fields.

**Acceptance Criteria:**
- [ ] Government and Private variants are distinct in copy/fields.
- [ ] Captures product category, specs, quantity, timeline, contact.
- [ ] Validations prevent malformed submissions.
- [ ] Submissions persist reliably in transactional database.

**Dependencies:** REQ-007.

#### REQ-005: Persistent WhatsApp Integration (Non-Blocking UX)
**Description:** Provide persistent click-to-chat across hub/spokes while ensuring no obstruction of RFQ interaction on mobile.

**Acceptance Criteria:**
- [ ] Floating/persistent CTA available site-wide.
- [ ] RFQ screens have obstruction-safe CTA behavior.
- [ ] WhatsApp click events are tracked to GA4.

**Dependencies:** Frontend event layer.

#### REQ-006: Project Portfolio First-Class Feature
**Description:** Portfolio must be a core navigation feature with structured entries and filters.

**Acceptance Criteria:**
- [ ] Minimum 20 structured entries before Phase 1 launch approval.
- [ ] Entries include project type, client category, location, scope, outcome.
- [ ] Portfolio pages link contextually to relevant spokes.

**Dependencies:** Content operations readiness.

#### REQ-007: Centralized Lead + RFQ Data Pipeline
**Description:** All inbound RFQs/leads from all domains flow into one centralized transactional system.

**Acceptance Criteria:**
- [ ] PlanetScale schema supports lead lifecycle fields and source attribution.
- [ ] All submission endpoints write successfully with retry/error handling.
- [ ] Dashboard reflects near-real-time updates.

**Dependencies:** DB schema + API layer.

#### REQ-008: SEO Migration & Redirect System
**Description:** Preserve SEO equity by complete 301 migration from legacy domains to new hub/spoke architecture.

**Acceptance Criteria:**
- [ ] URL mapping table exists for indexed/high-value pages.
- [ ] Legacy URLs without direct mapping must fallback 301 to nearest parent category or spoke homepage (never unresolved 404 during migration window).
- [ ] Canonical rules are implemented on new pages.

**Dependencies:** SEO mapping audit + edge routing config.

#### REQ-009: Notification Workflow for Lead Operations
**Description:** New RFQs/leads trigger operational notifications.

**Acceptance Criteria:**
- [ ] Transactional email via Resend for RFQ acknowledgment and internal notice.
- [ ] Telegram alert for internal near-real-time follow-up.

**Dependencies:** REQ-007.

#### REQ-010: Authenticated Admin Dashboard
**Description:** Centralized dashboard for lead/RFQ management using NextAuth.js.

**Acceptance Criteria:**
- [ ] Secure login and protected routes.
- [ ] Lead list with filter/search/source tags.
- [ ] Segment-based views and export-ready structure.

**Dependencies:** REQ-007.

### Should Have (P1)

#### REQ-011: Documentation Library Expansion
Includes richer technical library (datasheets, guides, compliance references) with indexing/filtering.

#### REQ-012: Product Comparison Tool
Basic comparison for selected product categories.

### Nice to Have (P2)

#### REQ-013: ROI Calculator and IoT Showcase
Advanced pre-sales tooling and smart-city capability presentation.

---

## Non-Functional Requirements

### Performance
- Mobile PSI score target: **90+** on key templates.
- Page response should support sub-second TTFB target using edge delivery.
- Core templates must pass Core Web Vitals thresholds.
- Large media and document assets must not degrade UX or induce layout shift.

### Scalability
- Multi-subdomain support from one codebase/deployment model.
- Content growth for portfolio/docs without major restructuring.
- Reliable handling of campaign spikes without downtime.

### Reliability
- RFQ submission path must be resilient; no silent submission loss.
- If API/DB failure occurs, graceful fallback with pre-filled WhatsApp handoff is mandatory.
- Alerting for submission failures must be enabled.

### Security
- Auth-protected admin dashboard (NextAuth.js).
- Least-privilege data access for internal roles.
- Input validation and anti-spam for RFQ endpoints.
- TLS and secure data handling for lead records.

### Accessibility & UX
- Responsive/mobile-first UX across hub and spokes.
- Persistent WhatsApp CTA must not block RFQ form fields or submit actions.

### Maintainability
- Single unified codebase (monorepo/headless architecture), no disconnected spoke codebases.
- Shared UI component library and tokenized design system.

---

## Technical Considerations

### Architecture (Locked)
- **Model:** Hub-and-Spoke Sub-domain Architecture.
- **Hub:** Corporate trust center + portfolio + certifications + routing.
- **Spokes:** Product-cluster sub-domains with shared templates/design.
- **Codebase:** Greenfield single monorepo.

### Locked Stack
- **Framework:** Next.js 14+ (App Router)
- **Monorepo:** Turborepo
- **CMS:** Sanity.io
- **UI:** Tailwind CSS + Radix UI
- **Data:** Sanity (content source of truth) + PlanetScale (transactional leads/users)
- **Auth:** NextAuth.js
- **Hosting/Delivery:** Cloudflare Pages (+ edge network/runtime usage)
- **Notifications:** Resend + Telegram Bot
- **Analytics:** GA4 + GSC + Cloudflare Analytics

### Integration Requirements (Locked)
1. Legacy SEO mapping + 301 redirect orchestration.
2. Cross-domain lead integration with source attribution.
3. Sanity-driven content federation for hub/spokes.
4. Resend + Telegram communications.
5. Unified analytics instrumentation across root and sub-domains.
6. WhatsApp click-to-chat integration + GA4 event tracking.

### Migration/Data Pipeline Constraints
- Legacy WordPress content requires cleansing/sanitization to remove malformed HTML/shortcodes before publishing via Sanity + Next.js rendering.

---

## Implementation Roadmap

## Milestone Plan (Locked)
- **Total Duration:** 1 month
- **Milestones:** 1
- **Sprints:** 2

### Sprint 1 (Weeks 1–2): Core Foundation + Migration Safety
**Objectives:**
- Monorepo + hub/spoke routing baseline
- SEO mapping and redirect engine
- Core RFQ backend and data pipeline
- Certifications hub MVP

### Sprint 2 (Weeks 3–4): Launch-Ready MVP Hardening
**Objectives:**
- Portfolio (minimum 20 entries)
- Dashboard + notifications + auth
- Performance optimization and CWV/PSI conformance
- QA, error fallback, and launch gate validation

---

## Out of Scope

Given strict 1-month timeline, defer the following:
1. Complex decorative animations and non-critical visual effects.
2. Advanced comparison logic beyond MVP scope.
3. Full ROI calculator (Phase 2/3).
4. Deep IoT showcase experience (Phase 2/3).
5. Any feature that risks core migration, RFQ reliability, or trust infrastructure readiness.

---

## Open Questions & Risks

### Open Questions
1. Final sub-domain naming convention approval (`pju.`, `lightning.`, etc.).
2. Exact baseline values for some KPI targets requiring pre-launch audit snapshot.
3. Ownership model for ongoing content governance post-launch.

### Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Scope creep under 1-month timeline | High | High | Strict MVP control; defer non-critical features |
| SEO loss due to incomplete mapping | Medium | Critical | Full URL mapping + tested fallback redirect logic |
| RFQ technical failure causing lead loss | Medium | Critical | Graceful error handling + pre-filled WhatsApp fallback |
| Legacy content breaks frontend rendering | High | High | Sanitization/validation pipeline before publish |
| Performance regression from heavy assets | Medium | High | Next Image optimization + Sanity CDN + lazy loading |

---

## Validation Checkpoints

### Checkpoint 1 (End of Sprint 1)
- [ ] Hub and at least one spoke routing operational.
- [ ] 301 mapping framework + fallback logic implemented.
- [ ] RFQ pipeline writes to DB successfully.
- [ ] Certifications hub MVP live in staging.

### Checkpoint 2 (Mid Sprint 2)
- [ ] Admin dashboard auth and lead listing functional.
- [ ] Notifications working (Resend + Telegram).
- [ ] WhatsApp integration tracked via GA4.

### Checkpoint 3 (Pre-Launch Final)
- [ ] Minimum 20 portfolio entries completed.
- [ ] Mobile PSI target 90+ on key templates.
- [ ] CWV checks pass acceptable thresholds.
- [ ] RFQ fallback behavior validated under forced failure test.
- [ ] SEO migration QA sign-off completed.

---

## Appendix: Task Breakdown Hints

### Suggested Task Bundle (for Taskmaster parsing)
1. Monorepo + shared UI foundation
2. Multi-subdomain routing and environment config
3. Sanity schema for products, certs, portfolio, docs
4. Hub templates + trust sections
5. Spoke templates + product rendering
6. RFQ API + DB schema + validations
7. Dashboard auth + lead views
8. Notification pipelines (Resend + Telegram)
9. WhatsApp persistent CTA + tracking events
10. SEO URL inventory + redirect mapping
11. Redirect fallback engine (no unmapped 404 edge case)
12. Legacy content ingestion + sanitization pipeline
13. Portfolio population (20 minimum)
14. Performance tuning (edge/runtime, media optimization)
15. QA/UAT + launch checklist

### Dependency Highlights
- 1 → 2 → 4/5
- 3 → 4/5/13
- 6 → 7/8
- 10 → 11 → Launch
- 12 → Content publishing quality
- 14 + 15 required before go-live

### Complexity Estimate
- Overall complexity: **Complex**
- Timeline mode: **Compressed (1 month, 2 sprints)**
- Delivery strategy: **Strict MVP with risk guardrails**

---

**End of PRD**

This PRD reflects all finalized discovery answers, including locked architecture, technical stack, timeline, integration priorities, and explicit migration/performance risk controls.