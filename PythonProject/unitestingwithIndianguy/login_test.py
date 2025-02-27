import pytest
from playwright.sync_api import Page, expect, BrowserContext


@pytest.fixture(autouse=True)
def visit_test_page(page:Page):
    page.goto("http://uitestingplayground.com/sampleapp")


def test_successful_login(page:Page, context:BrowserContext):
    username = "dan"
    password = "pwd"

    username_field = page.get_by_placeholder("User Name")
    password_field = page.get_by_placeholder("********")

    login_button = page.locator("#login")

    username_field.fill(username)
    password_field.fill(password)
    login_button.click()

    success_status = page.locator("label.text-success")
    expect(success_status).to_have_text(f"Welcome, {username}!")

def test_wrong_password(page:Page):
    username = "dan"
    password = "pwds"

    username_field = page.get_by_placeholder("User Name")
    password_field = page.get_by_placeholder("********")
    login_button = page.locator("#login")

    username_field.fill(username)
    password_field.fill(password)
    login_button.click()

    status = page.locator("label.text-danger")
    expect(status).to_have_text("Invalid username/password")