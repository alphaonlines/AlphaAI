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
