import asyncio
from asyncio import wait_for

from playwright.async_api import  Playwright,async_playwright,expect



async def run(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=1500)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://playwright.dev/python/docs/intro")
    await expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    menu_list_item =  page.locator("ul.menu__list")
    menu_list_item_writing_test = menu_list_item.locator('a:has-text("Writing tests")')
    await expect(menu_list_item_writing_test).to_be_visible()
    # await page.get_by_role("link", name ="Writing tests", exact=True).click()
    await menu_list_item_writing_test.click()
    await expect(page.locator('#introduction')).to_contain_text("Introduction")
    element_p = page.locator('p strong:has-text("You will learn")')
    await expect(element_p).to_be_visible()

    await context.close()
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())