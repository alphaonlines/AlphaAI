# AlphaAI Market & Innovation Timeline (v3.2)

## 🎯 Project Goal
To visualize the evolution of technology from raw metallurgy to AGI, focusing on the **market impact**, **related products**, and **industrial foundations** (batteries, robotics, AI).

## 📜 Data Rules (The Schema)
Every entry in `timeline.json` must follow this structure:
1.  **year** (Integer): e.g., 1856
2.  **title** (String): Short event name.
3.  **visual** (Emoji): A representative icon.
4.  **summary** (String): One sentence overview.
5.  **market_analysis** (String): *New field.* Deep dive into products, stocks, or economic shifts.
6.  **wiki_url** (String): *New field.* Direct link to a relevant Wikipedia page.
7.  **products** (Array of Strings): *New field.* List of physical goods enabled by this tech (e.g., "Steel Beams", "Lithium Cells").

## ✅ Current Checklist
- [ ] **Design:** Remove sticky image, focus on text/data density.
- [ ] **Feature:** Make "Expand" dropdowns show Wikipedia links.
- [ ] **Content:** Add "Metallurgy/Industrial Revolution" era (1700s-1800s).
- [ ] **Content:** Add "Related Products" data to existing JSON.

## 🛠 Workflow
1.  Update `timeline.json` with new events (now hosted in separate repo: https://github.com/alphaonlines/AlphaPulse).
2.  Run `update_timeline.py` (if adding single entries) or edit JSON directly for bulk changes.
3.  (Optional) Pull recent headlines via GDELT:
    - List top stories:
      - `python3 fetch_gdelt.py`
    - Emit schema-ready JSON skeletons you can paste into `timeline.json`:
      - `python3 fetch_gdelt.py --as-timeline --max 10 > recent.json`
      - review/edit `recent.json`, then paste entries into `timeline.json`
4.  Refresh `index.html` to test.

## Swarm deploy on this host
- This machine's Swarm currently errors on `docker stack deploy` when it tries to auto-create an overlay network.
- Use the included service deploy helper instead:
  - `chmod +x deploy-swarm-service.sh`
  - `./deploy-swarm-service.sh`
- Defaults:
  - service name: `alphaai`
  - published port: `8087`
  - target node: `alphahs`
- Override them if needed:
  - `SERVICE_NAME=alphaai-alt PUBLISHED_PORT=8091 TARGET_NODE=alphahs ./deploy-swarm-service.sh`
