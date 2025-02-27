from pom_example_class import PlaywrightPage

from playwright.sync_api import Page, expect


def test_docs(page:Page):
    homepage = PlaywrightPage(page)
    homepage.visit_docs()
    expect(homepage.page).to_have_url("https://playwright.dev/python/docs/intro")

def test_search_assertions(page:Page):
    query = "assertions"
    homepage = PlaywrightPage(page)
    homepage.search(query)

    expect(homepage.search_results()).to_contain_text("List of assertions")
