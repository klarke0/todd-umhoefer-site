#!/usr/bin/env python3
"""
Todd Umhoefer Site — Notion Page Setup
Builds a clean content dashboard on the existing Notion page.
Uses only stdlib (urllib) — no pip install needed.

Usage:
  python3 notion-setup.py
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request

# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_PATH = os.path.join(SCRIPT_DIR, ".notion-token")
PAGE_ID = "33e1edbbdb9d80aa82a6ee6be7f177fb"
BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

if not os.path.exists(TOKEN_PATH):
    print(f"ERROR: Notion token not found at {TOKEN_PATH}")
    print("Create the file and paste your Notion integration token into it.")
    sys.exit(1)

with open(TOKEN_PATH) as f:
    TOKEN = f.read().strip()

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json",
}


def api_request(method, endpoint, payload=None):
    url = f"{BASE_URL}/{endpoint}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    for attempt in range(3):
        req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = int(e.headers.get("Retry-After", 2))
                print(f"  Rate limited — waiting {wait}s...")
                time.sleep(wait)
                continue
            body = e.read().decode("utf-8")
            print(f"ERROR {e.code}: {body}")
            sys.exit(1)
    print("ERROR: Failed after 3 retries")
    sys.exit(1)


# --- Block helpers ---

def text(content, bold=False):
    t = {"type": "text", "text": {"content": content}}
    if bold:
        t["annotations"] = {"bold": True}
    return t


def heading_2(content):
    return {"object": "block", "type": "heading_2", "heading_2": {"rich_text": [text(content)]}}


def heading_3(content):
    return {"object": "block", "type": "heading_3", "heading_3": {"rich_text": [text(content)]}}


def paragraph(content="", bold=False):
    rich = [text(content, bold=bold)] if content else []
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": rich}}


def divider():
    return {"object": "block", "type": "divider", "divider": {}}


def callout(content, emoji="💡", color="gray_background"):
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [text(content)],
            "icon": {"type": "emoji", "emoji": emoji},
            "color": color,
        },
    }


def bulleted(content):
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": [text(content)]},
    }


def todo(content, checked=False):
    return {
        "object": "block",
        "type": "to_do",
        "to_do": {"rich_text": [text(content)], "checked": checked},
    }


# --- Update page icon and title ---
print("Updating page metadata...")
api_request("PATCH", f"pages/{PAGE_ID}", {
    "icon": {"type": "emoji", "emoji": "🎨"},
    "properties": {
        "title": {"title": [{"type": "text", "text": {"content": "Todd Umhoefer — Site"}}]}
    },
})

# --- Build page blocks ---
print("Building page content...")

blocks = [
    callout(
        "toddumhoefer.com  ·  GitHub: klarke0/todd-umhoefer-site  ·  Netlify: toddsite.netlify.app",
        emoji="🌐",
        color="blue_background",
    ),
    paragraph(),
    divider(),

    heading_2("📋 Site Content"),
    paragraph("Copy and notes for each section. Reply to the project email with updates and the site will be edited to match."),
    paragraph(),
    heading_3("Hero / Banner"),
    paragraph("Name: Todd Umhoefer", bold=True),
    paragraph("Tagline: "),
    paragraph(),
    heading_3("About"),
    paragraph("Bio text goes here."),
    paragraph(),
    heading_3("Visual Art"),
    paragraph("Description / statement for the visual art section."),
    paragraph(),
    heading_3("Music"),
    paragraph("Description / statement for the music section."),
    paragraph(),
    heading_3("Contact"),
    paragraph("Contact email or preferred method of contact."),
    paragraph(),
    divider(),

    heading_2("🖼️ Image Assets"),
    paragraph("Links or uploads for photos and artwork to be used on the site."),
    paragraph(),
    bulleted("Profile / hero photo — "),
    bulleted("Art portfolio images — "),
    bulleted("Music press photo — "),
    bulleted("Logo or wordmark (if any) — "),
    paragraph(),
    divider(),

    heading_2("🎵 Music"),
    paragraph("Links to streaming profiles, releases, or embeds to feature on the site."),
    paragraph(),
    bulleted("Spotify — "),
    bulleted("SoundCloud / Bandcamp — "),
    bulleted("Apple Music — "),
    bulleted("Latest release — "),
    paragraph(),
    divider(),

    heading_2("✅ To-Do"),
    paragraph("Shared task list for Kevin and Todd."),
    paragraph(),
    todo("Send bio copy"),
    todo("Send hero photo"),
    todo("Decide on color palette / visual direction"),
    todo("Review site design mockup"),
    paragraph(),
    divider(),

    heading_2("🔧 Dev Notes"),
    paragraph("For Kevin's reference."),
    paragraph(),
    callout("Push to main on GitHub → Netlify auto-deploys to toddumhoefer.com", emoji="⚡", color="yellow_background"),
    paragraph(),
    bulleted("Notion page ID: 33e1edbbdb9d80aa82a6ee6be7f177fb"),
    bulleted("Notion token: .notion-token (gitignored — never commit)"),
    bulleted("GitHub: https://github.com/klarke0/todd-umhoefer-site"),
    bulleted("Netlify: https://app.netlify.com — site: toddsite"),
    bulleted("Daily cron agent: https://claude.ai/code/scheduled/trig_01MYCqgkRXTnXm93jQqkDCnu"),
]

api_request("PATCH", f"blocks/{PAGE_ID}/children", {"children": blocks})

print(f"\n✅ Done. View at: https://www.notion.so/Todd-s-Site-{PAGE_ID.replace('-', '')}")
