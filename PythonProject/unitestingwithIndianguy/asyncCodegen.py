import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://playwright.dev/python/docs/intro")
    await expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    await page.get_by_role("link", name="Writing tests",  ).click()
    await expect(page.get_by_role("heading", name="Writing tests")).to_be_visible()
    await page.get_by_role("link", name="Navigation", exact=True).click()
    await expect(page.locator("#navigation")).to_contain_text("Navigation")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
