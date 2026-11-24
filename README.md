# Experts' First Exam — public website

One file, `index.html`. It contains only public information:
domain and field names, illustrative example tasks, the scoring method and
the release plan. Fonts are built into the file, so the page loads nothing
from anywhere else. The proposal form is a Google Form that opens in a new tab.

EFE is one benchmark. It is made of 58 **domains**, grouped into 20 **fields**.

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
- `src/data.json`: everything the site shows (domains, fields, rules, figures)
- `src/build.py`: puts template, data and fonts together

To rebuild: `python3 src/build.py <fonts-folder> "<google-form-link>" index.html`.
Small text changes can also be made directly in `index.html` (search for
`const DATA`), but then copy them back into `data.json` too.

## Settings (top of the `<script>` in index.html)

- `orgEmail`: the project address (expertsfirstexam@gmail.com). Shown in the
  footer and on the Contribute page; the "Email us" button writes to it.
- `contactEmail`: the personal address. Shown next to the project address,
  and copied (cc) on messages sent with the "Email us" button.
- `googleFormUrl`: the task proposal form (opens in a new tab).
- `organizer`: who runs EFE, shown in the footer as "Organized by …".
  Empty hides the line.
- `releaseTarget`: the planned first release, e.g. `January 2027`. Shown on
  the home page, the Leaderboard page and in the footer.
- `githubUrl`, `paperUrl`: empty shows "coming soon" in the footer; add the
  link when it exists.
- `workspaceUrl`: address of the private workspace; empty hides "Team sign in".

## Pages

The menu is: Leaderboard · Domains · How it works, plus a Contribute button.

- **Home**: the wheel of domain tiles, then "Explore by field", a short
  "How a task is scored", and the Leaderboard and Contribute cards.
  - The current field's name sits right under its highlighted tiles, with
    arrows on each side to step through the fields (dragging the wheel also
    works). Clicking the name jumps to that field in "Explore by field".
  - The wheel does not move on its own. Pointing at a tile shows its example
    task; clicking a tile opens the domain's page. On phones the wheel is
    hidden.
  - "Explore by field" always shows the same field as the wheel.
- **Leaderboard** (`#/leaderboard`): release date, what the leaderboard will
  show, and how models are scored.
- **Domains** (`#/domains`): all domains by field, with search (names, fields
  and example tasks), a field dropdown and a Core / Joint filter. When a
  filter is on, it shows "Showing N of 58 domains".
- The browser's Back button returns to the same spot (and the same search or
  field). Arriving from a menu link starts fresh at the top.
- **Domain pages** (`#/d/<slug>`).
- **How it works** (`#/how`): the scoring diagram, the two scores, public and
  private tasks, and what makes a good task.
- **Contribute** (`#/contribute`): two paths (propose a task, or lead/partner
  on a domain), what happens next, and the checklist.
- Older addresses still work: `#/benchmarks`, `#/b/<slug>` and `#/results`.
  Any other address shows "Page not found".

## Content (`src/data.json`)

**`areas`**: the fields, in display order (`id`, `name`, `desc`). `desc` is the
one-line description shown in "Explore by field".
Colors follow this order around a color wheel, so neighbouring fields get
neighbouring colors and the wheel reads as one gradient. Keep related fields
next to each other. Adding, removing or moving a field recolors the rest
automatically. Each field also has a line drawing (14 are built in; a new
field id falls back to the generic one).

**`benchmarks`**: one entry per domain (the key keeps its old name):
- `slug`: its web address, `#/d/<slug>`
- `code`: the badge text
- `name`, `area` (a field id), `status`
- `shared`: `false` = **Core** (built by the EFE team; no tag on cards);
  `true` = **Joint** (co-built with a partner team): a solid orange "✱ Joint"
  badge on cards and pages, an orange ring and ✱ badge on its wheel tile, and
  a light orange tint on its card
- `example`: the illustrative task title shown on the wheel, in the field
  explorer and on the domain's page (replaced by the first entry of
  `examples` once filled)

Fill these in as content becomes ready; anything left empty shows a
placeholder on the domain's page:
- `description`: one paragraph for the Overview.
- `paper`: `{"title", "authors", "venue", "arxiv", "pdf", "code", "bibtex"}`
  (links; missing links show as greyed-out buttons).
- `examples`: up to 3 tasks, each `{"title", "steps": [...], "meta": [...]}`.
  Use only public tasks, never private ones.
- `taxonomy`: `[{"direction": "...", "categories": ["...", "..."]}]`.
- `team`: `{"leads": [...], "members": [...], "contributors": [...]}`.
  Names here are public: add people only with their agreement.

**`stats`**: `modelsTarget` (shown as written, e.g. "30–50").
**`seeking`**: fields looking for an expert partner (empty = a "Don't see your
field?" line instead). **`rules`**: the "What makes a good task" checklist.

## Security notes

- The page sets a Content-Security-Policy: it cannot load scripts, fonts,
  images or frames from anywhere else. If you later embed something (e.g. a
  form inside the page), add its address as `frame-src` in the `<meta
  http-equiv="Content-Security-Policy">` line, or it will be blocked.
- Only upload `index.html` and this README to the public repository. Never
  add the prototype, `schema.sql`, task files or anything private: a public
  repository is visible to everyone, and GitHub keeps every old version even
  after you delete a file.
