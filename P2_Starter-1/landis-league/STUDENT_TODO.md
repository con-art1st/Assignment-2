# Project 2 — TODO Checklist

Tick these off as you go. Point values match the rubric. All HTML is already
written — every item below is a CSS task against the classes already in the
markup.

## index.html — 20 pts
- [ ] `.site-header` / `.nav-link` styled, with a visible `:hover`/`:focus` state on nav links
- [ ] `.hero` has a background image or color, with the title and tagline readable on top of it
- [ ] `.game-grid` / `.game-card` laid out with Flexbox or Grid, consistent gaps and padding
- [ ] `.about-league` article has a comfortable reading width; `.about-photo` is styled
- [ ] `.spotlight` aside is visually distinct from ordinary body text (background, accent border, or both)
- [ ] `.map-embed` iframe is visually integrated (border-radius and/or shadow)
- [ ] `.site-footer` has a background color and organized layout for its two blocks

## schedule.html — 20 pts
- [ ] `.standings-table` header row is styled, rows alternate color (`:nth-child`), rows highlight on `:hover`
- [ ] `.games-table` shares the same table "look" as the standings table
- [ ] `.sport-grid` / `.sport-card` laid out responsively with Flexbox or Grid; cards have a hover effect
- [ ] `.term-list` (the glossary `<dl>`) clearly distinguishes `<dt>` from `<dd>`

## register.html — 20 pts
- [ ] All text/email/tel/number/select/textarea inputs share consistent padding, borders, and a visible `:focus` style
- [ ] `.form-section` fieldsets and their legends read as distinct grouped sections
- [ ] `.color-group` / `.swatch` styled so each jersey color is visible, and the checked radio's swatch is visually indicated (sibling selector off `:checked`)
- [ ] `.btn-primary` and `.btn-secondary` (submit/reset) are clearly different from each other, each with a hover state
- [ ] `.register-form` reads as one contained card
- [ ] `.registration-rules` aside styled consistently with the home page's `.spotlight`

## officiate.html — 15 pts
- [ ] `.role-article` / `.role-photo` styled consistently with `.about-league` on the home page
- [ ] `.roles-table` styled consistently with the schedule page's tables
- [ ] `.apply-form` styled consistently with `.register-form` — reuse your existing rules where the markup matches
- [ ] `.steps-list` has a custom visual treatment (not the plain browser `<ol>` numbering)

## Everything else — 25 pts
- [ ] **Layout & responsive (12):** Flexbox/Grid used for 2+ layout components; card grids reflow at narrow widths via `auto-fit`/`minmax()` or `flex-wrap`; no horizontal overflow at 375px
- [ ] **CSS technique & consistency (8):** one stylesheet linked identically everywhere; a reused `:root` custom property; class-based selectors only (no ids, no inline styles); 3+ pseudo-classes used somewhere
- [ ] **Code organization (5):** commented CSS sections, consistent indentation, `check_html.py` passes, no JS, no media files
