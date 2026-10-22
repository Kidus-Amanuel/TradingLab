# Contracts Package (`@tradinglab/contracts`)

This package forms the typed boundary between the Python FastAPI backend and the Next.js frontend.

## Workflow
1. The FastAPI backend exposes OpenAPI schema (or exports `backend/openapi.json`).
2. Running `pnpm codegen` generates static TypeScript types in `src/api-types.ts` via `openapi-typescript`.
3. The `frontend` package imports `@tradinglab/contracts` directly via the pnpm workspace (`workspace:*`).
4. Result: Zero manual interface duplication, guaranteed compile-time type safety across the stack.
