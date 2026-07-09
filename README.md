# InsightForge

> **Transform Excel into Trusted Business Intelligence**

InsightForge is an enterprise-grade AI-powered analytics platform that transforms spreadsheets into interactive dashboards, validated business metrics, and actionable insights.

Unlike traditional dashboard builders, InsightForge prioritizes **data accuracy, validation, reproducibility, and auditability** before visualization.

---

# Vision

Businesses run on Excel.

However, Excel-based reporting often suffers from:

- Manual calculations
- Broken formulas
- Duplicate data
- Inconsistent reports
- Difficult collaboration
- Lack of data validation
- Time-consuming dashboard creation

InsightForge aims to become the analytics engine that sits between raw business data and business decisions.

---

# Core Principles

- **Accuracy First** – Dashboards are only as good as the underlying calculations.
- **Validation Before Visualization** – Never build charts from invalid data.
- **Backend Owns Business Logic** – The frontend only renders results.
- **AI Assists, Never Calculates** – AI explains trends but never computes financial metrics.
- **Modular Architecture** – Every component should be replaceable and independently testable.
- **API First** – Every feature should be accessible via APIs.

---

# Product Goals

## MVP

- Upload Excel and CSV files
- Read multiple worksheets
- Validate datasets
- Detect schemas automatically
- Generate business metrics
- Generate dashboards
- Export reports
- Provide AI-generated business insights

## Future Goals

- Power BI Integration
- Tableau Integration
- Google Sheets Connector
- Database Connectors
- Scheduled Reports
- Collaboration
- Role-Based Access Control
- Forecasting
- Natural Language Analytics
- Multi-Tenant SaaS

---

# High-Level Architecture

```text
                   InsightForge Platform

                          │

     ┌────────────────────┼────────────────────┐

     ▼                    ▼                    ▼

 Data Sources       Analytics Engine      Presentation

     │                    │                    │

 Excel              Validation          HTML Dashboard

 CSV                Transformation      Power BI

 Database           Calculations        PDF

 APIs               Semantic Layer      Excel Export

 Google Sheets      AI Insights         REST API
```

---

# Planned Repository Structure

```text
InsightForge/

├── apps/
│   ├── api/
│   └── web/
│
├── packages/
│   ├── shared/
│   ├── ui/
│   ├── config/
│   ├── types/
│   └── python_shared/
│
├── infrastructure/
│   ├── docker/
│   ├── nginx/
│   ├── postgres/
│   └── redis/
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── database/
│   └── development/
│
├── scripts/
│
├── .github/
│   └── workflows/
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Technology Stack

## Backend

- Python 3.12
- FastAPI
- SQLAlchemy 2
- PostgreSQL
- Redis
- Polars
- Pandas
- OpenPyXL
- DuckDB
- Alembic
- Pydantic v2
- Loguru

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Apache ECharts
- AG Grid
- TanStack Query
- React Router

## Infrastructure

- Docker
- Docker Compose
- Nginx
- GitHub Actions
- Ruff
- Black
- MyPy
- Pytest

---

# Development Roadmap

## Phase 0 — Product Discovery ✅

- Product Vision
- Requirements
- Architecture
- Domain Model
- Development Standards
- Roadmap

---

## Sprint 1 — Platform Foundation

- Monorepo
- FastAPI
- React
- PostgreSQL
- Redis
- Docker
- GitHub Actions
- Logging
- Configuration
- Health APIs

---

## Sprint 2 — Dataset Management

- File Upload
- Dataset Storage
- Versioning
- Metadata
- Hashing
- Preview APIs

---

## Sprint 3 — Excel Engine

- Multi-sheet Support
- CSV Support
- Header Detection
- Schema Detection
- Metadata Extraction

---

## Sprint 4 — Validation Engine

Detect:

- Missing Values
- Duplicate Rows
- Duplicate IDs
- Invalid Dates
- Currency Mismatches
- Data Type Issues
- Empty Columns
- Outliers

Generate detailed validation reports.

---

## Sprint 5 — Semantic Layer

Convert technical column names into business concepts.

Example:

```
cust_id  → Customer ID
inv_amt  → Invoice Amount
inv_dt   → Invoice Date
```

---

## Sprint 6 — Calculation Engine

Support:

- Revenue
- Cost
- Profit
- Profit Margin
- Gross Margin
- Monthly Revenue
- Monthly Cost
- Quarterly Metrics
- Yearly Metrics
- Growth %
- Running Totals
- Weighted Average
- Rolling Average
- Budget vs Actual
- Variance Analysis

Every calculation will:

- Be implemented once
- Have unit tests
- Be deterministic
- Use Decimal for financial calculations

---

## Sprint 7 — Dashboard Definition Engine

Generate dashboard JSON containing:

- KPI Cards
- Charts
- Tables
- Filters
- Layout

---

## Sprint 8 — Dashboard Renderer

React application featuring:

- Dashboard Layout
- KPI Cards
- Interactive Charts
- Tables
- Global Filters
- Drill-down
- Dark Mode

---

## Sprint 9 — Export Engine

Export to:

- PDF
- Excel
- CSV
- JSON

---

## Sprint 10 — AI Insights

Generate:

- Executive Summaries
- Trend Analysis
- Anomaly Detection
- KPI Explanations
- Recommendations

> AI never performs business calculations.

---

## Sprint 11 — Integrations

- Power BI
- Tableau
- Google Sheets
- REST APIs
- Database Connectors

---

## Sprint 12 — Production Readiness

- Monitoring
- Security
- Performance Optimization
- Background Workers
- Deployment
- Documentation

---

# Future Plugin Architecture

```text
Analytics Engine

├── Data Connectors
│   ├── Excel
│   ├── CSV
│   ├── Google Sheets
│   ├── PostgreSQL
│   ├── SQL Server
│   └── REST APIs
│
├── Validation Plugins
│
├── Calculation Plugins
│
├── Dashboard Renderers
│   ├── HTML
│   ├── Power BI
│   ├── Tableau
│   └── PDF
│
└── AI Providers
    ├── OpenAI
    ├── Anthropic
    ├── Gemini
    └── Local LLM
```

---

# Engineering Standards

- Clean Architecture
- SOLID Principles
- Modular Monolith
- Repository Pattern
- Service Layer
- Dependency Injection
- API First
- Fully Typed Code
- Automated Testing
- CI/CD
- Structured Logging
- Immutable Source Data
- Reproducible Calculations

---

# Success Criteria

InsightForge should enable a user to:

1. Upload a dataset.
2. Validate its quality.
3. Understand its structure.
4. Compute trusted business metrics.
5. Generate an interactive dashboard.
6. Export reports.
7. Receive AI-generated business insights.

---

# Long-Term Vision

InsightForge is more than a dashboard generator.

The goal is to build an extensible analytics platform that combines:

- Data Validation
- Business Calculations
- Interactive Dashboards
- AI-Assisted Analysis
- Enterprise Integrations

into a single platform that organizations can trust for operational and business reporting.