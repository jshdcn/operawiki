#!/usr/bin/env python3
"""operawiki internal link checker.

Usage:
  python3 check-links.py [FILE ...]

With no arguments, scans every .md file in the repo (excluding .git, .github,
_site). With file arguments, scans only those files. Verifies that every
relative markdown link points to a file that exists. Prints a report of
broken links and exits 1 if any are found, so CI fails the PR.

CI policy:
- On pull_request: scan only the .md files changed in the PR, so pre-existing
  broken links on main do not block unrelated PRs.
- On push to main: scan the whole repo.

Design notes:
- Links starting with http(s)/mailto are skipped (external links are checked
  separately by lychee in the advisory job).
- Anchors (#fragment) are ignored here; heading anchors are not checked.
- Absolute-style links (/docs/x.md) are resolved against the repo root.
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP_DIRS = {".git", ".github", "_site", "node_modules"}

LINK_RE = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")


def collect_md_files():
    md_files = set()
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md"):
                md_files.add(os.path.relpath(os.path.join(root, f), REPO))
    return md_files


def check_file(f, md_files, broken):
    path = os.path.join(REPO, f)
    if not os.path.isfile(path):
        print(f"WARNING: file not found: {f}")
        return
    text = open(path, encoding="utf-8").read()
    for m in LINK_RE.finditer(text):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("/"):
            resolved = target[1:]
        else:
            base = os.path.dirname(f)
            resolved = os.path.normpath(os.path.join(base, target)) if base else target
        if resolved not in md_files:
            broken.setdefault(f, []).append(target)


def main():
    md_files = collect_md_files()
    if len(sys.argv) > 1:
        targets = [a for a in sys.argv[1:] if a.endswith(".md")]
        if not targets:
            print("No markdown files to scan.")
            return
        scanned = targets
    else:
        scanned = sorted(md_files)

    broken = {}
    for f in scanned:
        check_file(f, md_files, broken)

    if broken:
        print("Broken internal links found:")
        for f in sorted(broken):
            for t in broken[f]:
                print(f"  {f} -> {t}")
        sys.exit(1)

    print(f"OK: no broken internal links ({len(scanned)} file(s) scanned, "
          f"{len(md_files)} markdown files in repo).")


if __name__ == "__main__":
    main()
