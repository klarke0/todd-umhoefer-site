# Todd Umhoefer Site — Infrastructure Design

**Date:** 2026-04-10  
**Status:** Approved

---

## Overview

A static HTML/CSS/JS artist portfolio site for Todd Umhoefer (visual artist + musician), hosted on Netlify, version-controlled on GitHub, with a Notion page for content management. Infrastructure mirrors the Dog.Vibes pattern with one addition: GitHub is used for version control and Netlify is connected directly to the repo for automatic deploys.

---

## Repository

- **Repo name:** `todd-umhoefer-site`
- **Owner:** Kevin's GitHub account
- **Branch strategy:** `main` = production; all changes merge to `main`
- **Initial file structure:**
  ```
  /
  ├── index.html
  ├── styles.css
  ├── animations.js
  ├── images/
  └── docs/
      └── superpowers/
          └── specs/
  ```

---

## Deployment

- **Host:** Netlify
- **Connection:** OAuth to GitHub repo — auto-deploy triggers on every push to `main`
- **Publish directory:** repo root
- **Build command:** none (static files, no build step)

---

## Domain

- **Domain:** `toddumhoefer.com`
- **Registrar:** Squarespace
- **DNS configuration (same as Dog.Vibes):**
  - A record: `@` → `75.2.60.5`
  - CNAME: `www` → `[netlify-site-name].netlify.app`
- **SSL:** Free via Netlify / Let's Encrypt (auto-provisioned after DNS verified)

---

## Notion

- **Location:** Dedicated page in Kevin's Notion workspace
- **Access:** Shared with Todd (edit access)
- **Purpose:** Content dashboard — text copy, image asset links, page notes, to-dos
- **API:** Notion integration with `.notion-token` file (same pattern as Dog.Vibes)
- **Connection to site:** Manual reference only in Phase 1; automated in Phase 2 (see below)

---

## Cron / Content Sync (Phase 2 — future)

A Claude Code cron script will be added after the site design and build are complete.

- **Trigger:** Scheduled cron that monitors the Notion page for content changes
- **Behavior on change:** Edits the relevant site files, commits to `main`, pushes to GitHub
- **Result:** Netlify auto-deploy completes the content update loop
- **Credential pattern:** Reads Notion token from `.notion-token` file (not committed to repo)

---

## What Is Out of Scope for This Phase

- No backend, no database, no build tools
- No Make.com automations
- No Notion-to-site sync (Phase 2)
- Site design and visual implementation (separate spec)
