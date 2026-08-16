# Facebook Messenger Bulk Deleter

A Python + Playwright utility that automates bulk deletion of Messenger chats from the Facebook web UI.

---

## ⚠️ DISCLAIMER — READ BEFORE USE

**Use this tool entirely at your own risk.**

- This project is **not affiliated with, endorsed by, or supported by Meta/Facebook**.
- Automating interactions with Facebook may **violate Facebook's Terms of Service** and can result in **account restrictions, temporary locks, or permanent bans**.
- **Deleted chats cannot be recovered.** This tool permanently removes conversations from your account.
- Facebook frequently changes its web UI. Selectors in this script **may stop working without notice**.
- The local browser profile (`fb_playwright_profile/`) stores your **login session and authentication tokens**. Never share or commit this folder.
- The authors and contributors accept **no liability** for data loss, account action, or any other damages arising from use of this software.

By running this script, you acknowledge that you understand these risks and accept full responsibility for your actions.

---

## Requirements

- Python 3.9+
- [Playwright](https://playwright.dev/python/) with Chromium

## Setup

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# Install dependencies
pip install playwright

# Install the Chromium browser
playwright install chromium
```

## Usage

1. Run the script:

   ```bash
   python delete_messenger_chats.py
   ```

2. A Chromium window opens to Messenger. **Log in manually** if you are not already authenticated.

3. Make sure your **chat list sidebar is visible** on the left.

4. Return to the terminal and press **ENTER** to begin deletion.

5. The script deletes chats in batches of **50**, clicking through each chat's "More options → Delete chat" flow automatically.

6. When no more chats are found, the script stops and reports the total deleted.

7. Press **ENTER** again to close the browser.

## How It Works

- Uses a **persistent Playwright browser profile** (`fb_playwright_profile/`) so you only need to log in once.
- Targets the first visible chat in the sidebar on each iteration.
- Dismisses common pop-up dialogs (e.g. "Don't restore messages") before each batch.
- Processes up to `BATCH_LIMIT` (50) chats per batch, then continues until the list is empty.

## Security Notes

- `fb_playwright_profile/` is listed in `.gitignore` and **must never be pushed to GitHub** or shared.
- Do not run this on untrusted or shared machines while logged in.
- Consider logging out and deleting the profile folder when you are finished.

## Troubleshooting

| Problem | Suggestion |
|---|---|
| Script can't find chats | Ensure the Messenger sidebar is open and chats are loaded |
| "Delete chat" menu not found | Facebook may have changed its UI — update selectors in the script |
| Account warning from Facebook | Stop immediately; continued automation increases ban risk |
| Login keeps expiring | Delete `fb_playwright_profile/` and log in fresh |

## License

Provided as-is with no warranty. Use responsibly.
