# InsightForge Architecture

## Overview

InsightForge is a SaaS platform that transforms Excel workbooks into interactive dashboards and AI-powered insights.

The backend follows Clean Architecture principles, where each layer has a single responsibility.

---

## Architecture

Browser
    │
    ▼
FastAPI
    │
    ▼
API Layer
    │
    ▼
Service Layer
    │
    ▼
Repository Layer
    │
    ▼
PostgreSQL

Storage is accessed independently through the Storage Service.

---

## Layers

### API

Responsible for:

- Request validation
- Response serialization
- Authentication
- Calling services

API routes never access the database directly.

---

### Services

Responsible for business logic.

Examples:

- Upload Workbook
- Process Workbook
- Generate Dashboard
- Export Report

Services coordinate repositories and storage.

---

### Repositories

Responsible only for persistence.

Repositories:

- never access files
- never import FastAPI
- never perform business logic

---

### Storage

Responsible for storing files.

Supported providers:

- Local Storage
- Cloudflare R2 (planned)

The rest of the application communicates only with StorageService.

---

## Database

Current entities

- Workbook

Future entities

- User
- Workspace
- Worksheet
- Dashboard
- Report
- UsageEvent

---

## Development Workflow

Model

↓

Migration

↓

Repository

↓

Service

↓

API

↓

Frontend