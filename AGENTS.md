# Repository Guidelines

## Project Structure & Module Organization
- Static site; no build step. Entry pages live at `index.html`, `ai-overview.html`, `infrastructure.html`, and `research.html`.
- Shared styling sits in `assets/css/styles.css`; `assets/img/` and `assets/js/` are available for media or future scripts.
- Navigation uses relative links. When adding a page, place the new `.html` in the repo root and update each nav block for consistency.
- Executive plan: see `EXECUTIVE_PLAN.md` for the reader-first layout, sitemap, and content patterns to follow.

## Build, Test, and Development Commands
- Local preview (no install required): `python -m http.server 8000` then open `http://localhost:8000`.
- Basic link check: open pages in a browser and verify nav targets resolve; Chart.js loads from the CDN in `ai-overview.html`.
- Optional: run `npx serve .` if you prefer a node-based static server.

## Coding Style & Naming Conventions
- HTML: 2-space indentation, lowercase tags/attributes, descriptive text content; keep sections wrapped in semantic containers (`section`, `main`, `footer`).
- CSS: 2-space indentation; prefer updating the variables in `:root` for palette/spacing changes before adding new colors.
- Assets: name files in `kebab-case` (e.g., `ai-infra-graphic.png`); keep shared styles in `assets/css/styles.css` and avoid inline styles unless scoped examples demand it.

## Testing Guidelines
- Smoke test each page in a desktop and mobile viewport; confirm sticky nav, cards, and tables render without overflow.
- Validate charts: ensure the `<canvas id="marketShareChart">` remains present and Chart.js script tag remains intact when modifying `ai-overview.html`.
- After edits, reload via your local server to confirm gradients, typography, and spacing remain legible.

## Commit & Pull Request Guidelines
- Commits: concise, imperative subject lines (e.g., `Add robotics section to infrastructure page`); group related HTML/CSS changes together.
- Pull requests: summarize the change, list pages touched, and include before/after screenshots for visual updates. Note any CDN dependency additions.
- Link related issue/ticket IDs in the description; call out manual test steps performed (e.g., `Viewed index.html in Safari/Chrome mobile emulation`).

## Security & Configuration Notes
- Keep external scripts limited to trusted CDNs; current dependency is `https://cdn.jsdelivr.net/npm/chart.js` in `ai-overview.html`.
- No secrets or API keys should be embedded; this is a static site meant for GitHub Pages. If adding integrations, gate configuration through environment variables and documented placeholders rather than hardcoding.
