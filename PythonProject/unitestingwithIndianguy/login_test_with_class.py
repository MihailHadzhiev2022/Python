from playwright.sync_api import Page,expect

from login_class import LoginPage


def test_successful(page:Page):
    username = "dan"
    password = "pwd"

    login_page = LoginPage(page)

    login_page.login(username,password)

    expect(login_page.success_status).to_have_text(f"Welcome, {username}!")

def test_fail(page:Page):
    username = "dan"
    password = "pwdsss"

    login_page = LoginPage(page)
    login_page.login(username, password)
    expect(login_page.status).to_have_text("Invalid username/password")

