from playwright.sync_api import Page,expect


def test_dynamic_button(page:Page):
    url = "http://uitestingplayground.com/dynamicid"

    page.goto(url)

    button_dynamic = page.get_by_role('button', name="Button with Dynamic ID")
    expect(button_dynamic).to_be_visible()

    h3_element = page.locator('.container', has_text="Dynamic ID")
    expect(h3_element).to_contain_text("Dynamic ID")

    h4_element = page.locator('h4', has_text="Scenario")
    expect(h4_element).to_be_visible()
    h4_play = page.locator('.container', has_text="Playground")
    expect(h3_element).to_be_visible()

    hrefche = page.get_by_role('link', name="Fork the website on GitHub")
    expect(hrefche).to_be_visible()
    hrefche.click()
    expect(page).to_have_url("https://github.com/inflectra/ui-test-automation-playground")
    code = page.locator('.prc-Button-Label-pTQ3x', has_text="Code")
    code.click()
