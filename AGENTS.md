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
