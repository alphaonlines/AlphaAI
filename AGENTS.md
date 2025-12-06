# AI for Beginners - Repository Guidelines

## Project Structure & Module Organization
- Static site; no build step. Entry pages live at `index.html`, `getting-started.html`, and `daily-life.html`.
- Shared styling sits in `assets/css/styles.css`; `assets/img/` is available for images.
- Navigation uses relative links. When adding a page, place the new `.html` in the repo root and update each nav block for consistency.
- Target audience: Older adults (50+) who are new to AI, especially on mobile devices.

## Build, Test, and Development Commands
- Local preview (no install required): `python -m http.server 8000` then open `http://localhost:8000`.
- Basic link check: open pages in a browser and verify nav targets resolve.
- Mobile testing: Use browser dev tools to test on various phone screen sizes.
- Optional: run `npx serve .` if you prefer a node-based static server.

## Coding Style & Naming Conventions
- HTML: 2-space indentation, lowercase tags/attributes, simple and clear text content; keep sections wrapped in semantic containers (`section`, `main`, `footer`).
- CSS: 2-space indentation; prefer updating the variables in `:root` for palette/spacing changes before adding new colors.
- Assets: name files in `kebab-case` (e.g., `beginner-guide.png`); keep shared styles in `assets/css/styles.css` and avoid inline styles.

## Content Guidelines
- Writing style: 8th-grade reading level maximum, simple language, short sentences.
- Tone: Friendly, reassuring, encouraging - avoid technical jargon.
- Structure: One concept per section, use bullet points for easy scanning.
- Examples: Use relatable, everyday situations that older adults will recognize.

## Accessibility Requirements
- Large default font (18px minimum) with font size controls
- High contrast mode available
- Large touch targets (44px minimum for interactive elements)
- Screen reader friendly with proper ARIA labels
- Mobile-first responsive design
- Simple, consistent navigation

## Testing Guidelines
- Smoke test each page in desktop and mobile viewports; confirm navigation, cards, and buttons render properly.
- Test accessibility features: font size controls, high contrast mode, keyboard navigation.
- Verify all links work and navigation is consistent across pages.
- Test on actual mobile devices when possible.
- After edits, reload via your local server to confirm readability and accessibility.

## Commit & Pull Request Guidelines
- Commits: concise, imperative subject lines (e.g., `Add safety tips to getting-started page`); group related HTML/CSS changes together.
- Pull requests: summarize the change, list pages touched, and include before/after screenshots for visual updates.
- Note accessibility testing performed (e.g., `Tested font size controls and high contrast mode`).

## Security & Configuration Notes
- No external scripts or dependencies beyond Google Fonts.
- No secrets or API keys should be embedded; this is a static site meant for GitHub Pages.
- All AI tool links should go to official, reputable sources only.
- Privacy-focused: no tracking, analytics, or third-party cookies.
