# The Ed Answer Key — Conversation Finder CF3.1 Release Candidate

This folder is the GitHub-ready static build for **The Ed Answer Key** Conversation Finder.

## Runtime files
- `index.html` — complete site and Conversation Finder interface
- `conversations.json` — production episode, taxonomy, question, and recommendation data
- `assets/brand-mark.png` — self-contained favicon/touch icon asset

## Maintenance
- `docs/PUBLISHING-WORKFLOW.md` — Episode 57+ editorial and publishing workflow
- `docs/episode-intake-template.json` — structured intake template for a new episode
- `scripts/validate-conversations.py` — structural validator for `conversations.json`

## Validate before deployment
From this directory:

```bash
python scripts/validate-conversations.py conversations.json
```

Expected result:

```text
PASS
areas=7 questions=21 finderEligible=55
```

## Deployment
This is a static site. Keep `index.html` and `conversations.json` in the same directory. The Finder loads `./conversations.json` over HTTP/HTTPS and contains an identical embedded fallback for local-file viewing.

If this folder lives inside the SageGap repository as `/ed-answer-key/`, GitHub Pages/Cloudflare can serve it at the corresponding `/ed-answer-key/` path without a framework build step.

## Release state
Branch/build: `51.3.11-CF3.1-QA-validated`.

`PLAYER-001` from CF3.0 is patched: closing the Finder audio player clears its cached catalog ID, and reopening the same episode reloads its RSS audio source.

The production data has passed structural validation. Treat this commit as the **CF3.1 release candidate** until the final deployed-browser regression pass is completed on the hosted URL.
