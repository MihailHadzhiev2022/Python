from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.page.goto("http://uitestingplayground.com/sampleapp")
        self.username_field = self.page.get_by_placeholder("User Name")
        self.password_field = self.page.get_by_placeholder("********")

        self.login_button = self.page.locator("#login")

        self.success_status = self.page.locator("label.text-success")
        self.status = self.page.locator("label.text-danger")

    def login(self,username,password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
