# Arsitektur Informasi (Information Architecture)
## DBSN Centralized Digital Ecosystem — sentradaya.com

**Versi:** 1.0  
**Tanggal:** 2026-04-24  
**Berbasis:** PRD v3.0  
**Status:** Final Draft — Siap untuk Tim UI/UX

---

## Ikhtisar

Dokumen Arsitektur Informasi ini mendefinisikan organisasi, pelabelan, navigasi, dan sistem findability untuk ekosistem digital DBSN yang dibangun di atas arsitektur **Hub-and-Spoke**. Semua label menggunakan **Bahasa Indonesia** formal.

### Arsitektur Domain

```
sentradaya.com                    → Hub (Pusat Kepercayaan Korporat)
├── pju.sentradaya.com            → Spoke: PJU - Penerangan Jalan Umum
├── solarcell.sentradaya.com      → Spoke: Panel Surya
├── alatpetir.sentradaya.com      → Spoke: Penangkal Petir
├── baterai.sentradaya.com        → Spoke: Baterai
└── dashboard.sentradaya.com      → Portal Layanan Pelacakan (Autentikasi)
```

### Segmen Pengguna

| Segmen | Persona | Kebutuhan Utama |
|--------|---------|-----------------|
| **B2G** | PPK, Staf Pengadaan, BUMN | Validasi SNI/TKDN/LKPP → Portofolio → RFQ Formal |
| **B2B** | Procurement, EPC, Facility Manager | Riset Spesifikasi → Datasheet → RFQ atau WhatsApp |

---

## Dokumen IA

Arsitektur Informasi terbagi dalam 3 dokumen:

### 1. [Strategi & Sistem Navigasi Global](./ia-strategy-navigation.md)
- Strategi IA dan prinsip desain untuk model Hub-and-Spoke
- Header navigasi: Hub, Spoke, dan Dashboard
- Footer global
- Elemen persisten (WhatsApp CTA, Breadcrumb, Trust Badge)

### 2. [Sitemap Hub, Spoke, & Dashboard](./ia-sitemaps.md)
- **Hub Sitemap** — 7 halaman utama: Beranda, Tentang Kami, Pusat Sertifikasi, Portofolio, Produk, RFQ, Kontak
- **Spoke Sitemap (Template)** — Kedalaman 3 level: Lini Produk → Sub-kategori → Detail Produk (PDP)
- **Dashboard Sitemap** — Portal autentikasi: Login, Pelacakan (tab Proyek/Pesanan), Profil
- Struktur URL dan komponen PDP

### 3. [Alur Pengguna Inti](./ia-user-flows.md)
- **Alur B2G** — Validasi legalitas → Verifikasi portofolio → RFQ formal → Dashboard pelacakan
- **Alur B2B** — Riset produk → Unduh datasheet → RFQ/WhatsApp → Dashboard pelacakan
- **Alur Fallback** — Penanganan kegagalan API dengan WhatsApp pre-filled
- Perbandingan touchpoint dan GA4 event mapping

---

## Keputusan IA Kunci

| Keputusan | Detail |
|-----------|--------|
| **Sertifikasi Matriks** | Berdasarkan tipe di Hub, berdasarkan produk di Spoke PDP |
| **Kedalaman Produk** | 3 level: Lini → Sub-kategori → PDP |
| **RFQ Mandiri** | Halaman dedicated `/permintaan-penawaran` dengan pre-fill URL params |
| **Dashboard Phase 1** | Pelacakan status saja (daftar tunggal + tab filter) |
| **Bahasa** | Bahasa Indonesia formal untuk semua label navigasi |

---

*Dokumen ini adalah indeks utama. Baca setiap bagian secara berurutan untuk pemahaman lengkap.*
