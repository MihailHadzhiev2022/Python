from playwright.sync_api import  Page,expect


def test_scroll(page:Page):
    page.goto("http://uitestingplayground.com/scrollbars")


    btn = page.get_by_role('button', name="Hiding Button")
    btn.scroll_into_view_if_needed()
    page.screenshot(path="test.jpg")