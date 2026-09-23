"""Creates the empty Rassed project layout. Run: python create_layout.py"""

from pathlib import Path

ROOT = Path("rassed")

README = """# Rassed

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
"""

GITIGNORE = """__pycache__/
*.py[cod]
.venv/
.env
.pytest_cache/
.ruff_cache/
node_modules/
dist/
data/raw/*
!data/raw/.gitkeep
services/vision/model/*.onnx
services/vision/model/*.pt
"""

FILES = {
    # Root
    "README.md": README,
    ".gitignore": GITIGNORE,
    ".env.example": "# Environment variables (copy to .env). Never commit real secrets.\n",
    "docker-compose.yml": "# Services: postgres (postgis + pgvector), redpanda, minio, api, ingestion, vision\n",
    ".github/workflows/ci.yml": "# CI: lint + tests for each service, build for each frontend\n",
    # Docs
    "docs/architecture.md": "# Architecture\n",
    "docs/green-it.md": "# Green IT decisions and measurements\n",
    "docs/data-privacy.md": "# Data privacy (anonymization, EXIF, INPDP)\n",
    # API
    "services/api/Dockerfile": "# API image\n",
    "services/api/pyproject.toml": "# API dependencies and tool config (ruff, pytest)\n",
    "services/api/app/__init__.py": "",
    "services/api/app/main.py": '"""FastAPI app creation and router registration."""\n',
    "services/api/app/core/__init__.py": "",
    "services/api/app/core/config.py": '"""Settings loaded from environment variables."""\n',
    "services/api/app/core/database.py": '"""Async database engine and session."""\n',
    "services/api/app/core/security.py": '"""Password hashing and JWT tokens."""\n',
    "services/api/app/core/storage.py": '"""MinIO image storage."""\n',
    "services/api/app/models/__init__.py": "",
    "services/api/app/models/base.py": '"""SQLAlchemy declarative base."""\n',
    "services/api/app/models/enums.py": '"""Roles, waste categories, blind-spot statuses, site types."""\n',
    "services/api/app/models/entities.py": '"""Tables: users, zones, sensitive_sites, sources, observations, blind_spots, reports, rag_chunks."""\n',
    "services/api/app/schemas/__init__.py": "",
    "services/api/app/schemas/auth.py": '"""Auth request/response schemas."""\n',
    "services/api/app/schemas/report.py": '"""Citizen report schemas."""\n',
    "services/api/app/schemas/blindspot.py": '"""Blind-spot schemas."""\n',
    "services/api/app/schemas/kpi.py": '"""KPI response schemas."""\n',
    "services/api/app/routers/__init__.py": "",
    "services/api/app/routers/deps.py": '"""Shared dependencies: current user, role checks."""\n',
    "services/api/app/routers/auth.py": '"""Register and login endpoints."""\n',
    "services/api/app/routers/reports.py": '"""Citizen report endpoints."""\n',
    "services/api/app/routers/blindspots.py": '"""Blind-spot list, detail and actions."""\n',
    "services/api/app/routers/kpis.py": '"""KPI endpoints for the dashboard."""\n',
    "services/api/app/routers/rag.py": '"""Intervention assistant endpoint."""\n',
    "services/api/app/services/__init__.py": "",
    "services/api/app/services/geo.py": '"""H3 cell helpers."""\n',
    "services/api/app/services/persistence.py": '"""Decides when observations become a blind spot."""\n',
    "services/api/app/services/scoring.py": '"""Criticality score computation."""\n',
    "services/api/app/services/verification.py": '"""Citizen report verification."""\n',
    "services/api/tests/test_persistence.py": '"""Tests for persistence logic."""\n',
    "services/api/tests/test_scoring.py": '"""Tests for scoring logic."""\n',
    # Ingestion
    "services/ingestion/Dockerfile": "# Ingestion image\n",
    "services/ingestion/requirements.txt": "# Ingestion dependencies\n",
    "services/ingestion/virtual_camera/__init__.py": "",
    "services/ingestion/virtual_camera/replay.py": '"""Replays images/videos from data/virtual_cameras at a sampling interval."""\n',
    "services/ingestion/virtual_camera/change_gate.py": '"""Perceptual-hash check to skip unchanged frames."""\n',
    "services/ingestion/producers/__init__.py": "",
    "services/ingestion/producers/producer.py": '"""Publishes image pointer messages to Redpanda."""\n',
    "services/ingestion/anonymizer/__init__.py": "",
    "services/ingestion/anonymizer/anonymizer.py": '"""Face and license-plate blurring."""\n',
    "services/ingestion/tests/test_change_gate.py": '"""Tests for change gating."""\n',
    # Vision
    "services/vision/Dockerfile": "# Vision image\n",
    "services/vision/requirements.txt": "# Vision dependencies\n",
    "services/vision/consumer.py": '"""Consumes frame pointers, runs inference, stores observations."""\n',
    "services/vision/inference.py": '"""ONNX Runtime model loading and prediction."""\n',
    "services/vision/model/.gitkeep": "",
    "services/vision/training/train.py": '"""YOLO nano fine-tuning."""\n',
    "services/vision/training/export_onnx.py": '"""Export to ONNX and INT8 quantization."""\n',
    "services/vision/training/dataset.yaml": "# Dataset paths and class names\n",
    "services/vision/tests/test_inference.py": '"""Tests for inference."""\n',
    # RAG
    "services/rag/requirements.txt": "# RAG dependencies\n",
    "services/rag/ingest_docs.py": '"""Chunks and embeds documents into pgvector."""\n',
    "services/rag/finetune_embed.py": '"""Fine-tunes the embedding model."""\n',
    "services/rag/retriever.py": '"""Similarity search over rag_chunks."""\n',
    "services/rag/generator.py": '"""Generates recommendations from retrieved context."""\n',
    # Frontends (scaffold later with npm create vite)
    "apps/dashboard/.gitkeep": "",
    "apps/citizen-pwa/.gitkeep": "",
    # Data
    "data/raw/.gitkeep": "",
    "data/zones/.gitkeep": "",
    "data/rag_corpus/.gitkeep": "",
    "data/virtual_cameras/cameras.yaml": "# Virtual cameras: id, name, lat, lon, source folder, sample interval\n",
    # ML and green IT
    "ml/notebooks/.gitkeep": "",
    "ml/eval/.gitkeep": "",
    "green/measure.py": '"""CodeCarbon measurement helpers."""\n',
}


def main() -> None:
    for relative_path, content in FILES.items():
        path = ROOT / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Created {len(FILES)} files in ./{ROOT}")


if __name__ == "__main__":
    main()