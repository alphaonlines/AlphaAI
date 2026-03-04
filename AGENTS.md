# AlphaAI – Agent Notes

This repo is a static timeline viewer plus a small helper script.

## Files
- `index.html`: Single‑page app that loads and renders `timeline.json`.
- `timeline.json`: Data source (array of events).
- `update_timeline.py`: CLI helper to append/sort timeline entries.

## Data schema
Each entry in `timeline.json` should include:
- `year` (int), optional `month` (string)
- `title`, `visual`, `summary` (strings)
- `market_analysis` (string)
- `products` (array of strings)
- `wiki_url` (string)

Extra fields are tolerated by the UI, but prefer keeping to the schema unless a new UI feature needs them.

## Local usage
- Open `index.html` directly in a browser, or serve it:
  - `python3 -m http.server 8000`
  - then visit `http://localhost:8000/index.html`
- If the JSON lives elsewhere, set `<body data-timeline-path="path/to/timeline.json">`.

## Updating the timeline
- Interactive add:
  - `python3 update_timeline.py` → option `1`
- Bulk edits:
  - Edit `timeline.json` directly.
  - Keep years as integers; newest entries appear first.

## Quick sanity checks
- Validate JSON parses:
  - `python3 - <<'PY'\nimport json; json.load(open('timeline.json','r',encoding='utf-8')); print('ok')\nPY`
- Python script syntax:
  - `python3 -m py_compile update_timeline.py`

## Style/conventions
- Keep `index.html` self‑contained (no build step).
- Prefer minimal DOM + vanilla JS.
- Avoid introducing external dependencies unless strictly needed.
- 2026-03-03 04:30 EST — Cross-project AGENTS sync completed. Swarm bs node target is four nodes total (alphabs, alphabs1, alphabs2, alphabs3). Duplicate alphabs swarm entry was removed (kept node ID nrrwqjfd7pz2f1qcbpi7lxhtd; removed duplicate ID 6n2b3tnizkp313jqv9vzmctcx). Installer baseline is version 2026.03.03-7 with sleep and power hardening in Linux/Windows/mac setup scripts. Commands run: find AGENTS inventory, docker node list/remove, targeted SSH checks, USB node identity checks. Tests: swarm membership and SSH checks run; no repo-specific unit/integration tests run in this repo.
- 2026-03-03 23:06 EST — Coordinated planning update for WOLF-FD employee access rollout. Added a phased implementation checklist in `/home/alphahs/WOLF-FD/EMPLOYEE_ACCESS_TODO.md` covering login/session auth, role-based module permissions, lead assignment, CRM/message-board comments, and security/audit hardening. No AlphaAI runtime code changed this round.
- 2026-03-03 23:17 EST — Cross-repo status note: WOLF-FD Phase 1 employee auth/login shipped live with cookie sessions, protected backend API routes, seeded owner account, and frontend sign-in/sign-out flow. Supporting checklist updates were applied in `/home/alphahs/WOLF-FD/EMPLOYEE_ACCESS_TODO.md` and WOLF-FD `AGENTS.md`.
- 2026-03-03 23:32 EST — Cross-repo status note: WOLF-FD Phase 2 employee access shipped with Owner-managed user administration and role-based module visibility. Backend now supports role records, user-role assignment, owner-only admin user APIs, and authenticated password change; frontend now includes an Admin Users module for account create/roles/activation/reset and role-gated navigation. WOLF-FD AGENTS and employee rollout TODO were updated accordingly.
- 2026-03-03 23:37 EST — Cross-repo status note: WOLF-FD UI polish round shipped live to smooth jagged dashboard visuals. App shell and dashboard overview styling were refined (cleaner gradients, softer surfaces, tighter spacing rhythm, and smoother navigation states). Live bundle updated and health checks passed.
- 2026-03-03 23:43 EST — Cross-repo status note: WOLF-FD CRM page now includes an in-app `UPS List` section with add/check persistence for team priorities. Live deploy and health verification completed for this round.
- 2026-03-04 00:00 EST — Cross-repo status note: WOLF-FD CRM queue cleanup shipped live. The old CRM checklist/TODO block was removed and UPS was refactored into a cleaner structured up-list queue (priority, lane, owner, due date, status controls) with persisted browser storage. WOLF-FD build/deploy verification completed with live bundle `/fd/assets/index-D_NDCqA8.js` and passing health endpoint.
- 2026-03-04 00:10 EST — Cross-repo status note: WOLF-FD CRM page was fully reflowed for better usability. The layout now starts with Today-first follow-ups, then pipeline/contact operations, then UPS lane management and communication tools in a cleaner hierarchy. Live deployment and health verification completed with bundle `/fd/assets/index-xOal0M5A.js`.
- 2026-03-04 02:10 EST — Cross-repo status note: WOLF-FD CRM got a second UI pass with a new `Focused Rep Mode` toggle for tighter day-to-day execution. Focus mode surfaces follow-ups, quick UPS actions, selected lead editing, and template shortcuts while hiding heavier sections until switched back to full mode. Live deployment and health verification completed with bundle `/fd/assets/index-Cby-E65j.js`.
- 2026-03-04 02:14 EST — Cross-repo status note: WOLF-FD CRM blank-page hotfix shipped. Added defensive UPS localStorage schema normalization for legacy records and guarded lane grouping so older UPS entries no longer crash CRM rendering after UI mode updates. Live deploy + health verification completed with bundle `/fd/assets/index-BTryLlpa.js`.
- 2026-03-04 02:28 EST — Cross-repo status note: completed WOLF-FD dead-code/hygiene refactor pass. Removed orphan frontend files (legacy camera + firebase/gemini/data service modules), removed now-unused frontend deps (`@google/genai`, `firebase`, `dotenv`), cleaned backend unused symbols and removed tracked generated artifacts from `pos-dashboard-backend/src`, and added ignore rules to prevent artifact reintroduction. Frontend/backed TS + build validations passed.
- 2026-03-04 02:47 EST — Cross-repo status note: delivered WOLF-FD Phase 1 structural modularization (no behavior changes): backend parser/sql helpers extracted from monolithic `server.ts`, frontend sales + CRM UPS helpers extracted into dedicated utility modules, and large files reduced in size. Frontend/backend TS + build validations passed. Also recovered transient `/fd/api` 502 by reinstalling backend deps in `pos-dashboard-backend` and restarting PM2 `pos-api`; external health check returned `{"ok":true,"db":1}` post-fix.
- 2026-03-04 02:56 EST — Cross-repo status note: WOLF-FD Phase 2 structural refactor shipped for app-shell maintainability. `App.tsx` was decomposed into `components/app/*` modules (tab access/title config, nav item, auth screen, loading overlay, theme styles) with behavior preserved and file size reduced (1120→742 lines). Frontend/backend TS + build validations passed; current WOLF-FD footprint snapshot is 14,074 lines for TS/JS source and 21,570 lines across tracked code/docs/scripts.
- 2026-03-04 03:05 EST — Cross-repo status note: WOLF-FD Phase 3 refactor completed. Backend monolith reduction extracted Tasks/CRM APIs from `pos-dashboard-backend/src/server.ts` into route modules (`src/routes/tasksRoutes.ts`, `src/routes/crmRoutes.ts`), and frontend split moved SalesDashboard sortable-item + report math/types into dedicated modules (`components/sales/SortableItem.tsx`, `components/salesReportUtils.ts`). Validations passed (frontend/backend TS + builds). Updated WOLF-FD size snapshot: 13,916 TS/JS lines and 21,413 tracked code/docs/script lines.
- 2026-03-04 03:19 EST — Cross-repo status note: WOLF-FD Phase 4/5 refactor completed and validated. `WorkAdvertising.tsx` was modularized into `components/workAdvertising/types.ts` + `components/workAdvertising/utils.ts` (file reduced 1698→1267), and backend owner/admin APIs were extracted from `pos-dashboard-backend/src/server.ts` into `pos-dashboard-backend/src/routes/adminRoutes.ts` (server reduced 2475→2325). Frontend/backend TS + build checks passed. Updated WOLF-FD footprint snapshot: 13,864 TS/JS lines and 21,362 tracked code/docs/script lines.
- 2026-03-04 03:25 EST — Cross-repo status note: WOLF-FD Phase 6 refactor completed with backend auth route extraction (`pos-dashboard-backend/src/routes/authRoutes.ts`) and frontend Sales print modal extraction (`components/sales/SalesPrintDialog.tsx`). Core behavior preserved while reducing `server.ts` (2325→2268) and `SalesDashboard.tsx` (2893→2822). Frontend/backend TS + build checks passed before rollout.
- 2026-03-04 03:35 EST — Cross-repo status note: WOLF-FD Phase 7 refactor completed with SalesDashboard print drilldown extraction (`components/sales/SalesDrilldownPrintSections.tsx`) and backend sales-summary report extraction (`pos-dashboard-backend/src/routes/reportRoutes.ts`). Core behavior preserved while reducing `SalesDashboard.tsx` (2822→2610) and backend `server.ts` (2268→2096). Frontend/backend TS + build checks passed before rollout.
- 2026-03-04 03:49 EST — Cross-repo status note: WOLF-FD Phase 8 refactor completed with SalesDashboard core print table extraction (`components/sales/SalesCorePrintSections.tsx`) and backend analytics extraction (`pos-dashboard-backend/src/routes/analyticsRoutes.ts`) for `/api/low-margin`, `/api/summary`, and `/api/leaderboard`. Behavior preserved while reducing `SalesDashboard.tsx` (2610→2467) and backend `server.ts` (2096→1899). Frontend/backend TS + build checks passed before rollout.
- 2026-03-04 03:58 EST — Cross-repo status note: WOLF-FD Phase 9 refactor completed and prepared for rollout. Extracted the remaining interactive Sales report card from `components/SalesDashboard.tsx` into `components/sales/SalesReportCard.tsx` (SalesDashboard reduced 2467→2252) while preserving existing report filters/sorts and low-margin ticket links. Frontend/backend TS checks and builds passed (`npx tsc --noEmit --noUnusedLocals --noUnusedParameters`, `npm run build`). Updated WOLF-FD footprint snapshot: 14,486 TS/JS lines and 21,988 tracked code/docs/script lines.
- 2026-03-04 04:06 EST — Cross-repo status note: WOLF-FD Phase 10 refactor completed and prepared for rollout. Extracted backend sales-detail/items/Pro1st endpoints from `pos-dashboard-backend/src/server.ts` into `pos-dashboard-backend/src/routes/salesDetailRoutes.ts` and registered via dependency injection (`registerSalesDetailRoutes`). Behavior preserved while reducing backend `server.ts` from 1899 to 910 lines. Frontend/backend TS checks and builds passed (`npx tsc --noEmit --noUnusedLocals --noUnusedParameters`, `npm run build`).
- 2026-03-04 04:13 EST — Cross-repo status note: WOLF-FD Phase 11 refactor completed and prepared for rollout. Extracted the remaining backend insights endpoints from `pos-dashboard-backend/src/server.ts` into `pos-dashboard-backend/src/routes/insightsRoutes.ts` (`available-years`, `outliers`, `coverage-months`, `sales-weekly/daily`, and `sales-by-location`) with dependency-injected route registration (`registerInsightsRoutes`). Behavior preserved while reducing backend `server.ts` from 910 to 599 lines. Frontend/backend TS checks and builds passed (`npx tsc --noEmit --noUnusedLocals --noUnusedParameters`, `npm run build`).
- 2026-03-04 04:17 EST — Cross-repo status note: WOLF-FD Phase 12 refactor completed and prepared for rollout. Extracted core system endpoints (`/health` and `/api/import/upload`) from `pos-dashboard-backend/src/server.ts` into `pos-dashboard-backend/src/routes/systemRoutes.ts`, preserving existing upload/importer behavior through dependency-injected route registration (`registerSystemRoutes`). Behavior preserved while reducing backend `server.ts` from 599 to 548 lines. Frontend/backend TS checks and builds passed (`npx tsc --noEmit --noUnusedLocals --noUnusedParameters`, `npm run build`).
- 2026-03-04 04:29 EST — Cross-repo status note: WOLF-FD Phase 13 refactor completed and prepared for rollout. Extracted backend startup schema/bootstrap routines from `pos-dashboard-backend/src/server.ts` into `pos-dashboard-backend/src/startupBootstrap.ts` (`ensureAuthSchema`, `ensureDefaultRoles`, `ensureDefaultAuthUser`, `ensureCrmSchema`) and switched server startup to call `runStartupBootstrap(...)` with injected dependencies. Behavior preserved while reducing backend `server.ts` from 548 to 379 lines. Frontend/backend TS checks and builds passed (`npx tsc --noEmit --noUnusedLocals --noUnusedParameters`, `npm run build`).
- 2026-03-04 04:34 EST — Cross-repo status note: WOLF-FD Phase 14 refactor completed and prepared for rollout. Extracted backend auth/session helpers from `pos-dashboard-backend/src/server.ts` into `pos-dashboard-backend/src/authSessionUtils.ts` and `pos-dashboard-backend/src/authDb.ts`, then rewired auth/admin/bootstrap integrations to use the new modules with dependency injection. Behavior preserved while reducing backend `server.ts` from 379 to 235 lines. Frontend/backend TS checks and builds passed (`npx tsc --noEmit --noUnusedLocals --noUnusedParameters`, `npm run build`).
