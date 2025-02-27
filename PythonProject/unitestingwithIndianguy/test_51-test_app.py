from playwright.sync_api import Page
import pytest


DOCS_URL = "https://playwright.dev/python/docs/intro"

@pytest.fixture(autouse=True)
def visit_page(page:Page):
    page.goto("https://playwright.dev/python")

    return page

def test_page_has_get_started_link(page: Page):


    link = page.get_by_role("link", name="GET STARTED")
    link.screenshot(path="photo1.png")
    link.click()

    assert page.url == DOCS_URL

def test_page_drugo(page:Page):

    link = page.get_by_role("link", name="Docs")
    assert link.is_visible()