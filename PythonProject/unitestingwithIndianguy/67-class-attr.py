from playwright.sync_api import Page, expect


def test_dynamic_id(page: Page):
    page.goto("http://uitestingplayground.com/classattr")

    # css selector
    primary_btn = page.locator("button.btn-primary")


    xpath_button = page.locator("//button[contains(@class, 'btn-primary')]")
    # # xpath
    # primary_btn = page.locator(
    #     "//button[ contains(@class,  ]"
    # )

    expect(xpath_button).to_be_visible()

    primary_btn.click()