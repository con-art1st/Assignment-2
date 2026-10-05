#!/usr/bin/env python3
"""
check_html.py -- Project 2 (Landis League) structure checker

This project is graded on CSS, not HTML: the starter's markup is already
complete and correct, and every rubric hook (a class, an id, a form control)
depends on that markup staying in place. Deleting or renaming a tag to "make
the CSS easier" silently breaks the grader's selectors and costs you the
points tied to that section, even if the page looks fine in a browser.

Run this against your OWN working folder before you submit:

    python3 check_html.py /path/to/landis-league

It checks that every required element, class, and id from the starter is
still present in each page. It does NOT check your CSS -- passing this only
means the HTML skeleton wasn't broken. A page can pass every check here and
still lose CSS points on requirements this script can't see (media queries,
box-shadow, transitions, etc.) -- see STUDENT_TODO.md and the rubric for
those.

Exit code 0 = every check passed. Exit code 1 = something is missing, and
the report tells you exactly what and in which file.
"""
import sys
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit(
        "This script needs BeautifulSoup4. Install it with:\n"
        "  pip install beautifulsoup4"
    )

# Each entry: (human label, CSS selector, minimum number of matches required)
CHECKS = {
    "index.html": [
        ("shared header", "header.site-header", 1),
        ("nav with 4 links", "nav.main-nav a.nav-link", 4),
        ("hero section", "section.hero", 1),
        ("hero heading (h1)", "section.hero h1.hero-title", 1),
        ("register CTA button", "section.hero a.btn", 1),
        ("this-week section", "section.this-week", 1),
        ("game cards (4+)", "div.game-grid article.game-card", 4),
        ("about-league article", "article.about-league", 1),
        ("about-league photo", "article.about-league img", 1),
        ("champion spotlight aside", "aside.spotlight", 1),
        ("find-the-fields section", "section.visit", 1),
        ("titled map iframe", "section.visit iframe[title]", 1),
        ("shared footer", "footer.site-footer", 1),
    ],
    "schedule.html": [
        ("shared header", "header.site-header", 1),
        ("standings section", "section.standings", 1),
        ("standings table", "table.standings-table", 1),
        ("standings table caption", "table.standings-table caption", 1),
        ("standings header cells (scope)", "table.standings-table thead th[scope='col']", 4),
        ("standings row headers (scope)", "table.standings-table tbody th[scope='row']", 5),
        ("games section", "section.games", 1),
        ("games table", "table.games-table", 1),
        ("games table rows (6+)", "table.games-table tbody tr", 6),
        ("sports section", "section.sports", 1),
        ("sport cards (4+)", "div.sport-grid article.sport-card", 4),
        ("sport card photos", "article.sport-card img.sport-photo", 4),
        ("glossary section", "section.glossary", 1),
        ("glossary dl", "dl.term-list", 1),
        ("glossary terms (4+)", "dl.term-list dt", 4),
        ("shared footer", "footer.site-footer", 1),
    ],
    "register.html": [
        ("shared header", "header.site-header", 1),
        ("register form", "form.register-form", 1),
        ("team-info fieldset", "form.register-form fieldset.form-section", 2),
        ("sport select with optgroups", "select#sport optgroup", 2),
        ("jersey color radio group", "fieldset.color-group input[type='radio']", 4),
        ("color swatches", "span.swatch", 4),
        ("roster size number input", "input#roster-size[type='number']", 1),
        ("captain email input", "input#captain-email[type='email']", 1),
        ("required agreement checkbox", "input#agree[type='checkbox'][required]", 1),
        ("submit + reset buttons", "form.register-form button.btn", 2),
        ("registration rules aside", "aside.registration-rules", 1),
        ("shared footer", "footer.site-footer", 1),
    ],
    "officiate.html": [
        ("shared header", "header.site-header", 1),
        ("role articles (2+)", "article.role-article", 2),
        ("open positions table", "table.roles-table", 1),
        ("open positions rows (4+)", "table.roles-table tbody tr", 4),
        ("application form", "form.apply-form", 1),
        ("availability checkboxes", "fieldset.availability-group input[type='checkbox']", 3),
        ("start-date input", "input#start-date[type='date']", 1),
        ("required clinic checkbox", "input#apply-agree[type='checkbox'][required]", 1),
        ("next-steps ordered list", "ol.steps-list", 1),
        ("next-steps items (5+)", "ol.steps-list li", 5),
        ("shared footer", "footer.site-footer", 1),
    ],
}


def check_file(path: Path, checks):
    html = path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "html.parser")
    failures = []
    for label, selector, minimum in checks:
        found = len(soup.select(selector))
        if found < minimum:
            failures.append(
                f"    [MISSING] {label}: expected >= {minimum} matching "
                f"'{selector}', found {found}"
            )
    return failures


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python3 {sys.argv[0]} /path/to/landis-league")

    root = Path(sys.argv[1])
    if not root.is_dir():
        sys.exit(f"Not a folder: {root}")

    any_failures = False
    for filename, checks in CHECKS.items():
        page = root / filename
        print(f"{filename}:")
        if not page.exists():
            print(f"    [MISSING] file not found: {page}")
            any_failures = True
            continue
        failures = check_file(page, checks)
        if failures:
            any_failures = True
            for line in failures:
                print(line)
        else:
            print(f"    all {len(checks)} checks passed")
        print()

    if any_failures:
        print("RESULT: one or more structural checks failed. Fix the HTML above")
        print("before you keep styling -- your CSS selectors need this markup.")
        sys.exit(1)
    else:
        print("RESULT: all structural checks passed. This does not grade your")
        print("CSS -- it only confirms the markup the CSS depends on is intact.")
        sys.exit(0)


if __name__ == "__main__":
    main()
