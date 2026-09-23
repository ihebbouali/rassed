# Rassed

Municipal waste blind-spot detection platform for Menzel Jemil (Bizerte, Tunisia).

## Work plan

- [ ] Day 1  - docker-compose (postgres+postgis+pgvector, redpanda, minio), DB models, first migration
- [ ] Day 2  - API: auth with roles, citizen report upload
- [ ] Day 3  - Dataset: public sets + local photos, labeling (4 classes)
- [ ] Day 4  - Train YOLO nano, export ONNX INT8, measure with CodeCarbon
- [ ] Day 5  - Virtual camera replay + change gating + producer
- [ ] Day 6  - Vision consumer, anonymizer, persistence engine (H3)
- [ ] Day 7  - Criticality scoring + blind-spot lifecycle API
- [ ] Day 8  - Dashboard: map + criticality list
- [ ] Day 9  - Dashboard: actions + KPIs
- [ ] Day 10 - Citizen PWA: capture, compression, submission
- [ ] Day 11 - Citizen report verification
- [ ] Day 12 - RAG: corpus, embeddings fine-tune, retrieval eval
- [ ] Day 13 - RAG intervention assistant in dashboard
- [ ] Day 14 - Green-IT report, tests, docs, demo

## Notes

- Frontends: scaffold with `npm create vite@latest` (Svelte template) inside apps/dashboard and apps/citizen-pwa.
- Migrations: run `alembic init -t async alembic` inside services/api when you reach Day 1.
