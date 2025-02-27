from playwright.sync_api import sync_playwright,Page, expect

def test_ajax(page:Page):

    page.goto("http://uitestingplayground.com/ajax")

    btn = page.get_by_role('button', name='Button Triggering AJAX Request')
    btn.click()

    paragraph_success = page.locator('p.bg-success')
    paragraph_success.wait_for()
    expect(paragraph_success).to_be_visible()
    hrefche = page.locator('a[href="https://github.com/inflectra/ui-test-automation-playground"]')
    hrefche.click()
    expect(page).to_have_url("https://github.com/inflectra/ui-test-automation-playground")