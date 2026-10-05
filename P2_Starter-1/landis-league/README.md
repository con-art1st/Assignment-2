# Project 2 Starter — Landis League

CGS 3066 · Web Programming & Design · Florida State University

## What's in here

```
landis-league/
├── index.html         complete HTML, zero CSS
├── schedule.html       complete HTML, zero CSS
├── register.html       complete HTML, zero CSS
├── officiate.html       complete HTML, zero CSS
├── css/                empty — this is where styles.css goes
├── images/             placeholder art — you may ship it as-is
└── check_html.py        run this before you submit
```

**Every page's markup is finished.** This project is graded on CSS, not
HTML. Your only job is to create `css/styles.css` and link it — it's already
linked from every page's `<head>`, so as soon as you save a file at that path
with rules in it, you'll see the site change.

**No audio or video files.** Do not add an `.mp3`, `.mp4`, or any other media
file to your submission.

## How to start

1. Unzip this folder somewhere you'll remember. Don't work inside the zip.
2. Open `index.html` in a browser and in a text editor side by side. It will
   look completely plain — that's expected. Every heading, list, and table is
   sitting there in the browser's default styles, waiting on your CSS.
3. Open each page's `<head>` and note the classes already applied throughout
   the body — `game-card`, `sport-card`, `standings-table`, `form-section`,
   and so on. These are your selectors. **Do not rename, remove, or add
   classes, ids, or elements.** Style what's already there.
4. Work through `STUDENT_TODO.md` in whatever order you like — the pages
   share a lot of the same patterns (cards, tables, forms), so styling one
   thoroughly makes the next one faster.
5. Run `check_html.py` (see below) any time you want to confirm you haven't
   accidentally broken the markup.

## Running check_html.py

```
pip install beautifulsoup4      # once, if you don't already have it
python3 check_html.py landis-league
```

Point it at your project folder. It reports any required element or class
that's gone missing. It does **not** grade your CSS — a page can pass every
check here and still be unstyled. It only protects you from losing points to
an accidental HTML edit.

## Before you submit

- [ ] `python3 check_html.py landis-league` reports all checks passed
- [ ] Exactly one `css/styles.css`, linked identically on all four pages
- [ ] No `<style>` blocks, no `style=""` attributes anywhere
- [ ] No ids or inline styles used as styling hooks — classes only
- [ ] At least one `:root` custom property, reused more than once
- [ ] At least three different pseudo-classes used somewhere in the file
- [ ] Flexbox and/or Grid used for at least two different layout components
- [ ] Card grids reflow at narrow widths using `auto-fit`/`minmax()` or
      `flex-wrap` — resize your browser down to phone width and check
- [ ] No horizontal scrollbar on the page itself at 375px wide
- [ ] No `.mp3`, `.mp4`, or other media files anywhere in the folder
- [ ] You opened the site from the unzipped folder and clicked every nav link

## Notes

- The placeholder images name what they stand in for and carry their pixel
  dimensions, so you can drop in real art at the same size. Shipping them
  as-is is fine and costs you nothing.
- If you do replace them, use royalty-free sources (unsplash.com,
  placehold.co) and keep them inside `images/`, at the same relative paths.
- Style the map `<iframe>` from the outside (border, radius, shadow) — you
  cannot reach inside a third-party embed with your CSS, and you don't need
  to.
- Use **relative** paths only in your CSS (e.g. `url('../images/hero-fields.jpg')`).
  `C:\Users\you\Desktop\...` will not work on the grader's machine.
