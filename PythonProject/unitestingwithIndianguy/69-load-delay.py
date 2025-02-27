from playwright.sync_api import Page, expect


def test_load_delay(page: Page):
    page.goto("http://uitestingplayground.com/")

    button_link = page.get_by_role('link', name="Load Delay")
    button_link.click()

    btn = page.get_by_role('button', name="Button Appearing After Delay")
    btn.wait_for()
    expect(btn).to_be_visible()

    btn_dve = page.locator('h4', has_text="Playground")
    btn_dve.wait_for()
    expect(btn_dve).to_be_visible()

    btn_tr = page.locator('a[href="https://github.com/inflectra/ui-test-automation-playground"]')
    btn_tr.wait_for()
    btn_tr.click()
    expect(page).to_have_url("https://github.com/inflectra/ui-test-automation-playground")