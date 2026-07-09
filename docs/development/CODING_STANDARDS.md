# Coding Standards

## General

* Follow SOLID principles.
* Keep functions small and focused.
* Prefer composition over inheritance.
* Use descriptive names.
* Avoid duplicated business logic.

## Backend

* FastAPI
* SQLAlchemy 2
* Pydantic v2
* Type hints everywhere
* Repository Pattern
* Service Layer

Business logic belongs only in services.

## Frontend

* React
* TypeScript
* Functional components
* Custom hooks for reusable logic
* Feature-oriented organization

## Git

Branch strategy:

* `main`
* `develop`
* `feature/<feature-name>`

Commit format:

* `feat:`
* `fix:`
* `refactor:`
* `docs:`
* `test:`
* `chore:`

## Testing

Every business rule must have automated tests.

Financial calculations should use decimal arithmetic rather than floating-point values.

## Documentation

Every new module should include:

* Purpose
* Dependencies
* Public interfaces
* Future improvements
