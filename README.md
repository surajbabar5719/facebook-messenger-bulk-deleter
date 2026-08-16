# Facebook Messenger Bulk Deleter

A high-speed Python automation script using Playwright to bulk-delete Facebook Messenger chats. Meta does not provide a native bulk-delete feature, so this tool automates the manual deletion process directly via the web UI.

## ⚠️ Disclaimer
**For Educational Purposes Only.** 
Using automated scripts on Meta platforms violates their Terms of Service. Executing this script at high speeds or for prolonged periods may result in temporary action blocks or permanent account bans. Use this tool entirely at your own risk. The author is not responsible for any account penalties.

## Features
* **Session Persistence:** Saves your login and 2FA session locally so you don't have to re-authenticate on every run.
* **Auto-Batching & Reloading:** Deletes chats in batches of 50 and automatically refreshes the page to prevent memory leaks and React UI freezes.
* **High-Speed Execution:** Bypasses visual hover delays by dispatching DOM click events directly.

## Installation
1. Clone the repository and navigate to the directory.
2. Install dependencies:
   ```bash
   pip install playwright
   playwright install chromium
   ```

## Usage
1. Run the script:
   ```bash
   python delete_messenger_chats.py
   ```
2. A Chromium window opens to Messenger. **Log in manually** if prompted.
3. Ensure your **chat list sidebar is fully visible**.
4. Return to the terminal and press **ENTER** to start the high-speed 50-batch deletion.
5. The script deletes chats automatically in batches of 50 until no more chats are found.
6. Press **ENTER** again to close the browser when finished.

## Security
The `fb_playwright_profile/` directory stores your Facebook session cookies and authentication tokens. It is listed in `.gitignore` and **must never be committed to GitHub** or shared with anyone.

## License
Provided as-is with no warranty. Use responsibly.
