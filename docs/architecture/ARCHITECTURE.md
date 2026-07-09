# InsightForge Architecture

## Overview

InsightForge is an AI-powered analytics platform that converts spreadsheets into validated business intelligence.

The system is designed around a **Modular Monolith** architecture.

Core principles:

* Accuracy before visualization
* Validation before calculation
* Backend owns all business logic
* AI explains data but never calculates it
* API-first design
* Extensible plugin architecture

---

## High-Level Architecture

```text
                 Browser
                     │
                     ▼
            React Frontend (apps/web)
                     │
               REST API / HTTPS
                     │
                     ▼
           FastAPI Backend (apps/api)
                     │
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
 Data Layer     Business Layer   Infrastructure
                     │
                     ▼
               PostgreSQL / Redis
```

---

## Backend Layers

### API

Responsible for:

* Routing
* Request validation
* Authentication
* Response formatting

No business logic belongs here.

### Services

Contains all business logic.

Examples:

* Dataset Service
* Validation Service
* Calculation Service
* Dashboard Service

### Repositories

Responsible only for data access.

Repositories should never contain business rules.

### Database

Stores:

* Datasets
* Users
* Dashboards
* Validation Reports
* Metrics

### Utilities

Reusable helper functions.

---

## Future Modules

* Excel Engine
* Validation Engine
* Semantic Layer
* Calculation Engine
* Dashboard Engine
* AI Engine
* Export Engine
* Power BI Integration

---

## Design Goals

* Modular
* Testable
* Scalable
* Maintainable
* Production-ready
