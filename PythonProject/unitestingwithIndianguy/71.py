from playwright.sync_api import sync_playwright,Page,expect


def test_input_field(page:Page):
    page.goto("http://uitestingplayground.com/textinput")

    text_input = page.locator('h3', has_text="Text input")
    expect(text_input).to_be_visible()

    new_text = "Hello Mihail"
    set_new_button = page.get_by_label("Set New Button Name")
    set_new_button.fill(new_text)

    btn = page.locator('button.btn-primary')
    btn.click()
    expect(btn).to_have_text(new_text)