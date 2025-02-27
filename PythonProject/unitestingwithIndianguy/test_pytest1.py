import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/python/")
    # expect(page.get_by_role("heading", name="IntroductionDirect link to")).to_be_visible()
    # page.get_by_role("link", name="Writing tests", exact=True).click()
    # expect(page.get_by_role("heading", name="IntroductionDirect link to")).to_be_visible()
    # page.get_by_role("link", name="Trace viewer").first.click()

    dropdown_menu = page.locator('ul.dropdown__menu')

    expected_items = ["Python", "Node.js", "Java", ".NET"]

    # Loop through the list and check each item
    for item in expected_items:
        expect(dropdown_menu).to_contain_text(item)
        print(f"element is found {item}")