# BI Report Agent

[![CI](https://github.com/kogunlowo123/bi-report-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/bi-report-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Data Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Business intelligence report generation agent that builds reports from natural language requests, creates visualizations, schedules automated delivery, and translates business questions into analytical queries.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_report` | Generate a BI report from a natural language business question |
| `create_visualization` | Create a data visualization from a dataset |
| `schedule_delivery` | Schedule automated report delivery via email or Slack |
| `suggest_chart_type` | Suggest the best chart type for a given dataset and question |
| `build_dashboard` | Build a dashboard from multiple report components |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/reports/generate` | Generate report |
| `POST` | `/api/v1/reports/visualize` | Create visualization |
| `POST` | `/api/v1/reports/schedule` | Schedule delivery |
| `POST` | `/api/v1/reports/suggest-chart` | Suggest chart type |
| `POST` | `/api/v1/reports/dashboard` | Build dashboard |

## Features

- Report Generation
- Visualization Creation
- Automated Delivery
- Query Translation
- Template Management

## Integrations

- Tableau
- Looker
- Power Bi
- Metabase
- Superset

## Architecture

```
bi-report-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── bi_report_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Tableau + Looker + Power BI + Metabase**

---

Built as part of the Enterprise AI Agent Platform.
