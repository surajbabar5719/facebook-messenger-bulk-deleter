import re
import time
from playwright.sync_api import Playwright, sync_playwright

USER_DATA_DIR = "./fb_playwright_profile"
TARGET_URL = "https://www.facebook.com/messages/t/"
BATCH_LIMIT = 50


def run(playwright: Playwright) -> None:
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=USER_DATA_DIR,
        headless=False,
        args=["--disable-notifications", "--start-maximized"],
    )

    page = context.pages[0] if context.pages else context.new_page()
    page.goto(TARGET_URL)

    print("\n" + "=" * 50)
    print("1. Log in manually if needed.")
    print("2. Ensure your Messenger chat list is fully visible.")
    print("=" * 50 + "\n")

    input("Press ENTER to start the high-speed 50-batch deletion: ")

    total_deleted = 0

    while True:
        for dismiss_text in ["Don't restore messages", "Dismiss Chat history is", "Close"]:
            try:
                btn = page.get_by_role("button", name=re.compile(dismiss_text, re.IGNORECASE)).first
                if btn.is_visible(timeout=1000):
                    btn.click(force=True)
                    time.sleep(0.5)
            except Exception:
                pass

        batch_deleted = 0
        print(f"\n--- Starting new batch. Total deleted so far: {total_deleted} ---")

        while batch_deleted < BATCH_LIMIT:
            try:
                target_btn = page.get_by_role("button", name=re.compile(r"^More options for", re.IGNORECASE)).first

                if not target_btn.is_visible(timeout=1500):
                    first_row = page.locator('div[role="gridcell"], div[role="row"], a[href*="/messages/t/"]').first
                    if first_row.is_visible(timeout=1000):
                        first_row.hover(force=True)
                    else:
                        print("No more chats found in the sidebar.")
                        break

                target_btn.dispatch_event("click")

                delete_menu_item = page.get_by_text("Delete chat", exact=True).first
                delete_menu_item.wait_for(state="visible", timeout=1500)
                delete_menu_item.click(force=True)

                confirm_btn = page.get_by_role("button", name="Delete chat").last
                confirm_btn.wait_for(state="visible", timeout=1500)
                confirm_btn.click(force=True)

                batch_deleted += 1
                total_deleted += 1
                time.sleep(0.2)

            except Exception:
                break

        if batch_deleted == 0:
            print("\nAll done — no more chats found.")
            break

        print(f"Batch complete: {batch_deleted} deleted this batch.")

    print(f"\nFinished. Total chats deleted: {total_deleted}")
    input("Press ENTER to close the browser...")
    context.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
