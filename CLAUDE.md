# Todd Umhoefer Site — Project Context

## What This Is

Portfolio site for Todd Umhoefer, a visual artist and musician.
- **Live URL:** https://toddumhoefer.com
- **GitHub:** https://github.com/klarke0/todd-umhoefer-site
- **Netlify site:** toddsite.netlify.app
- **Push to `main` = auto-deploy via Netlify**

## Site Stack

Static HTML/CSS/JS — no framework, no build step. Publish directory is repo root.

Files:
- `index.html` — main page (only page for now)
- `styles.css` — all styles, uses CSS custom properties defined in `:root`
- `animations.js` — scroll-based animations via IntersectionObserver
- `images/` — site images (dv-logo.png, dv-logo-inverse.png are Dog Vibes email assets)

## Git / Deploy

```bash
# Standard push (credentials stored in macOS Keychain on Kevin's machine)
git add -A && git commit -m "..." && git push origin main

# Remote agent push (use token in prompt, remove after)
git remote set-url origin https://TOKEN@github.com/klarke0/todd-umhoefer-site.git
git push origin main
git remote set-url origin https://github.com/klarke0/todd-umhoefer-site.git
```

## Notion

- **Page:** https://www.notion.so/Todd-s-Site-33e1edbbdb9d80aa82a6ee6be7f177fb
- **Page ID:** `33e1edbbdb9d80aa82a6ee6be7f177fb`
- **Token:** stored in `.notion-token` (gitignored — never commit)
- **Integration:** same integration token as Dog.Vibes workspace

## Email Pipeline

- **Todd's email:** toddumhoefer@yahoo.com
- **Sending from:** kevin@thedogvibes.com (Gmail alias)
- **Logo assets for emails:**
  - Header (inverse/white): `https://toddumhoefer.com/images/dv-logo-inverse.png`
  - Signature (dark): `https://toddumhoefer.com/images/dv-logo.png`
- **Rules:**
  - Always identify as an AI project assistant — never as Kevin personally
  - Only discuss this project
  - Only create Gmail drafts — never send directly
  - Kevin reviews and sends all outgoing emails

## Cron Agent

A daily remote agent (runs at 9am America/Los_Angeles via claude.ai/code/scheduled) checks Gmail for emails from Todd, implements requested changes, and drafts follow-up responses. Trigger ID: `trig_01MYCqgkRXTnXm93jQqkDCnu`

## Design Direction

Not yet finalized — design brainstorm pending. Reference site: chiaraluzzana.com (bold editorial, full-bleed imagery, strong typography). Todd is both a visual artist and musician — the site should serve both identities.
