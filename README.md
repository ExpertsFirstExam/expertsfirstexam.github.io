# Experts' First Exam — public website

One file, `index.html`. It contains only public information:
domain names, planned figures from the design doc, and the scoring method.
Fonts are built into the file, so the page loads nothing from Google except
the embedded proposal form.

## Put it on GitHub Pages

1. On GitHub, create a **public** repository (for example `efe-bench`).
2. Upload `index.html` (and this README) to the repository's `main` branch.
3. Go to **Settings → Pages**. Under "Build and deployment", choose
   **Deploy from a branch**, branch `main`, folder `/ (root)`, and save.
4. After a minute the site is live at
   `https://<your-account>.github.io/efe-bench/`.

Own domain (optional): in **Settings → Pages → Custom domain**, enter it
(e.g. `efe-bench.org`), add the DNS records GitHub shows you at your domain
registrar, then tick **Enforce HTTPS** once it is offered.

## How the site is built

The published file is `index.html`. It is generated from the `src/` folder:

- `src/template.html`: layout, styles and code
- `src/data.json`: everything the site shows (benchmarks, areas, rules, figures)
- `src/build.py`: puts template, data and fonts together

To rebuild: `python3 src/build.py <fonts-folder> "<google-form-link>" index.html`.
Small text changes can also be made directly in `index.html` (search for
`const DATA`), but then copy them back into `data.json` too.

## Settings (top of the `<script>` in index.html)

- `contactEmail`: shown in the footer and on the Contribute page.
- `googleFormUrl`: the proposal form shown on the Contribute page.
- `workspaceUrl`: address of the private workspace; empty hides "Team sign in".
- `googleFormHeight`: height of the embedded form in pixels.

## What the home page shows

- **Ring of tiles**: every benchmark is a tile, grouped by field around a
  wheel. Clicking a field name (or resting the mouse on it) turns the wheel to that field;
  visitors can also drag it or use the arrows. Hovering a tile (or the first
  tap on a phone) flips up a card with an example task; clicking opens the
  benchmark's page.
- **Explore by field**: a list of the fields. Hovering or clicking one shows
  its drawing, its benchmarks (Core or Joint) and example tasks.
- **How a task is scored**, then the leaderboard and contribute cards.

## Content (`src/data.json`)

**`areas`**: the fields, in display order (`id`, `name`). Colors are spread
evenly around the color wheel in this order, so adding or removing a field
recolors the rest automatically. Each field also has a line drawing (14 are
built in; a new field id falls back to the generic one).

**`benchmarks`**: one entry per benchmark:
- `slug`: its web address, `#/b/<slug>`
- `code`: the badge text
- `name`, `area` (an area id), `status`
- `shared`: `false` = **EFE Core** (built by the EFE team: solid card, black
  CORE tag); `true` = **EFE Joint \*** (co-built with a partner team: dashed
  orange card with hatching, JOINT * tag)
- `example`: the illustrative task title shown on the tile's flip card and in
  the field explorer (replaced by the first entry of `examples` once filled)

Fill these in as content becomes ready; anything left empty shows a
placeholder on the benchmark's page:
- `description`: one paragraph for the Overview.
- `paper`: `{"title", "authors", "venue", "arxiv", "pdf", "code", "bibtex"}`
  (links; missing links show as greyed-out buttons).
- `examples`: up to 3 tasks, each `{"title", "steps": [...], "meta": [...]}`.
  Use only public tasks, never hidden ones.
- `taxonomy`: `[{"direction": "...", "categories": ["...", "..."]}]`.
- `team`: `{"leads": [...], "members": [...], "contributors": [...]}`.
  Names here are public: add people only with their agreement.

**`stats`**: `plannedTasks` and `modelsTarget` (shown as written, e.g. "30–50").
**`seeking`**: fields looking for an expert partner (empty = a "Don't see your
field?" card instead). **`rules`**: the "What makes a good task" list.

## Security notes

- The page sets a Content-Security-Policy: it may only show the Google Form
  from docs.google.com and cannot load scripts, fonts or images from anywhere
  else. If you later embed something new (e.g. a different form service),
  add its address to `frame-src` in the `<meta http-equiv=
  "Content-Security-Policy">` line, or it will be blocked.
- Only upload `index.html` and this README to the public repository. Never
  add the prototype, `schema.sql`, task files or anything private: a public
  repository is visible to everyone, and GitHub keeps every old version even
  after you delete a file.
