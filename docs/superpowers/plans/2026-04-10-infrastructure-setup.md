# Todd Umhoefer Site — Infrastructure Setup Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the full infrastructure for toddumhoefer.com — GitHub repo, placeholder site, Netlify auto-deploy, custom domain, and Notion content page.

**Architecture:** Static HTML/CSS/JS files in a GitHub repo; Netlify connected via OAuth auto-deploys on every push to `main`; custom domain `toddumhoefer.com` pointed at Netlify via Squarespace DNS; Notion page in Kevin's workspace serves as the content dashboard.

**Tech Stack:** Static HTML/CSS/JS, GitHub, Netlify, Squarespace DNS, Notion API

---

## File Structure

```
/
├── .gitignore
├── index.html          ← placeholder landing page
├── styles.css          ← base styles (empty for now)
├── animations.js       ← animation hooks (empty for now)
├── images/
│   └── .gitkeep
└── docs/
    └── superpowers/
        ├── specs/
        │   └── 2026-04-10-infrastructure-design.md
        └── plans/
            └── 2026-04-10-infrastructure-setup.md
```

---

### Task 1: Initialize Git repo and push to GitHub

**Files:**
- Create: `.gitignore`
- Create: `index.html` (placeholder)
- Create: `styles.css` (empty)
- Create: `animations.js` (empty)
- Create: `images/.gitkeep`

- [ ] **Step 1: Initialize git in the project root**

```bash
cd "/Users/kevin/Desktop/Work Spaces/Todd's Site"
git init
git branch -M main
```

Expected output: `Initialized empty Git repository in .../Todd's Site/.git/`

- [ ] **Step 2: Create .gitignore**

Create `/Users/kevin/Desktop/Work Spaces/Todd's Site/.gitignore` with this content:

```
.notion-token
.DS_Store
*.env
node_modules/
```

- [ ] **Step 3: Create placeholder index.html**

Create `/Users/kevin/Desktop/Work Spaces/Todd's Site/index.html` with this content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Todd Umhoefer</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <p>Coming soon.</p>
  <script src="animations.js"></script>
</body>
</html>
```

- [ ] **Step 4: Create empty styles.css**

Create `/Users/kevin/Desktop/Work Spaces/Todd's Site/styles.css` with this content:

```css
/* Todd Umhoefer — styles */
```

- [ ] **Step 5: Create empty animations.js**

Create `/Users/kevin/Desktop/Work Spaces/Todd's Site/animations.js` with this content:

```js
// Todd Umhoefer — animations
```

- [ ] **Step 6: Create images directory placeholder**

```bash
touch "/Users/kevin/Desktop/Work Spaces/Todd's Site/images/.gitkeep"
```

- [ ] **Step 7: Create GitHub repo and push**

```bash
cd "/Users/kevin/Desktop/Work Spaces/Todd's Site"
gh repo create todd-umhoefer-site --public --source=. --remote=origin --push
```

Expected output: GitHub repo URL printed, all files pushed to `main`.

- [ ] **Step 8: Verify on GitHub**

Open the URL printed in the previous step. Confirm `index.html`, `styles.css`, `animations.js`, `.gitignore`, and `docs/` are all visible on `main`.

- [ ] **Step 9: Commit**

```bash
cd "/Users/kevin/Desktop/Work Spaces/Todd's Site"
git add .gitignore index.html styles.css animations.js images/.gitkeep docs/
git commit -m "feat: initial project scaffold"
git push origin main
```

---

### Task 2: Connect Netlify to GitHub and deploy

**Note:** This task uses the Netlify CLI (`npx netlify-cli`). No Netlify account login is needed in advance — the CLI will open a browser window to authorize.

- [ ] **Step 1: Log in to Netlify CLI**

```bash
npx netlify-cli login
```

A browser window will open. Authorize with the Netlify account associated with Kevin's email. Return to the terminal when done.

Expected: `You are now logged into your Netlify account!`

- [ ] **Step 2: Initialize Netlify site linked to GitHub repo**

```bash
cd "/Users/kevin/Desktop/Work Spaces/Todd's Site"
npx netlify-cli init
```

When prompted:
- **"What would you like to do?"** → `Connect this directory to an existing Netlify site` OR `Create & configure a new site`
- **Site name:** `todd-umhoefer` (or leave blank for a random name — can be changed)
- **Build command:** leave blank (hit Enter)
- **Publish directory:** `.` (a single dot — repo root)
- **Deploy path:** confirm defaults

Expected: Netlify creates the site and links it to the GitHub repo. A `netlify.toml` may be created — if so, commit it.

- [ ] **Step 3: Commit netlify.toml if created**

```bash
cd "/Users/kevin/Desktop/Work Spaces/Todd's Site"
git add netlify.toml
git commit -m "chore: add netlify config"
git push origin main
```

If no `netlify.toml` was created, skip this step.

- [ ] **Step 4: Verify auto-deploy is wired up**

In a browser, go to `app.netlify.com` → your site dashboard. Under **Deploys**, confirm a deploy was triggered by the push to `main` and shows **Published**.

- [ ] **Step 5: Note the Netlify subdomain**

On the Netlify site dashboard, find the auto-generated URL (e.g. `todd-umhoefer-abc123.netlify.app`). Copy it — you'll need it for the DNS step.

---

### Task 3: Configure custom domain (toddumhoefer.com)

**Note:** DNS propagation can take up to 48 hours but usually resolves within minutes. Do not skip the verification step.

- [ ] **Step 1: Add custom domain in Netlify**

In `app.netlify.com` → your site → **Domain management** → **Add a custom domain** → enter `toddumhoefer.com` → confirm.

Netlify will show you the DNS records needed. Keep this browser tab open.

- [ ] **Step 2: Update DNS records in Squarespace**

1. Go to `squarespace.com` → log in
2. Navigate to **Settings → Domains → toddumhoefer.com → DNS Settings**
3. Delete any existing A records or CNAMEs pointing to Squarespace servers
4. Add the following records:

**A Record:**
- Host: `@` (or blank)
- Value: `75.2.60.5`
- TTL: default

**CNAME Record:**
- Host: `www`
- Value: `[your-netlify-subdomain].netlify.app` (from Task 2 Step 5)
- TTL: default

5. Save changes.

- [ ] **Step 3: Verify domain in Netlify**

Back in Netlify → Domain management → click **Verify** next to `toddumhoefer.com`.

If DNS hasn't propagated yet, try again in a few minutes. When verified, the domain status will show a green checkmark.

- [ ] **Step 4: Provision SSL certificate**

In Netlify → Domain management → **HTTPS** → click **Verify DNS configuration** → click **Provision certificate**.

Netlify provisions a free Let's Encrypt certificate automatically. Status should show **Certificate provisioned**.

- [ ] **Step 5: Confirm site is live**

Open `https://toddumhoefer.com` in a browser. You should see the placeholder "Coming soon." page served over HTTPS.

---

### Task 4: Set up Notion content page

**Note:** This task is mostly manual Notion steps. No code changes.

- [ ] **Step 1: Create Notion page**

In Kevin's Notion workspace:
1. Create a new top-level page titled **"Todd Umhoefer — Site"**
2. Add these sub-sections as headings:
   - **Site Content** — for text copy per page/section
   - **Image Assets** — links or uploads for photos, artwork images
   - **To-Do / Notes** — shared task list for Todd and Kevin

- [ ] **Step 2: Share with Todd**

Click **Share** (top right of the page) → Invite Todd by email → set permission to **Can edit**.

- [ ] **Step 3: Create Notion integration**

1. Go to `notion.so/my-integrations`
2. Click **+ New integration**
3. Name it `Todd Umhoefer Site`
4. Associate it with Kevin's workspace
5. Click **Submit** → copy the **Internal Integration Token**

- [ ] **Step 4: Connect integration to the page**

On the "Todd Umhoefer — Site" Notion page:
1. Click `...` (top right) → **Connections** → search for `Todd Umhoefer Site` → click to connect

- [ ] **Step 5: Store the Notion token**

Create the file `/Users/kevin/Desktop/Work Spaces/Todd's Site/.notion-token` and paste the integration token as plain text (no quotes, no newline formatting).

Verify `.notion-token` is in `.gitignore` (it was added in Task 1 Step 2 — double-check it's listed).

- [ ] **Step 6: Note the Notion page ID**

From the Notion page URL (e.g. `https://www.notion.so/Todd-Umhoefer-Site-abc123def456...`), copy the 32-character hex string at the end. Save it somewhere accessible (e.g. paste it into the "Notes" section of the Notion page itself) — it will be needed when the cron/content-sync script is built in Phase 2.

---

### Task 5: Final verification

- [ ] **Step 1: End-to-end deploy test**

Make a trivial change to `index.html` (e.g. change "Coming soon." to "Coming soon.."), commit, and push:

```bash
cd "/Users/kevin/Desktop/Work Spaces/Todd's Site"
git add index.html
git commit -m "chore: verify auto-deploy pipeline"
git push origin main
```

- [ ] **Step 2: Confirm Netlify auto-deploy triggered**

In `app.netlify.com` → Deploys — confirm a new deploy appeared and completed within ~30 seconds of the push.

- [ ] **Step 3: Confirm live site updated**

Open `https://toddumhoefer.com` and hard-refresh (`Cmd+Shift+R`). Confirm the updated text is visible.

- [ ] **Step 4: Revert trivial change**

```bash
cd "/Users/kevin/Desktop/Work Spaces/Todd's Site"
# Edit index.html back to "Coming soon."
git add index.html
git commit -m "chore: revert test change"
git push origin main
```

Infrastructure is fully operational. Ready for Phase 2: site design and build.
