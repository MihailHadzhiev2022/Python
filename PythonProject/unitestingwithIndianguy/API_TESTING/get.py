from playwright.sync_api import  sync_playwright,Page,expect


def test_api_get(page:Page):
    response = page.request.get("https://jsonplaceholder.typicode.com/users")
    assert response.status == 200
    data = response.json()

    def print_user_by_id(user_id):
        return next(user for user in data if user["id"] == user_id)

