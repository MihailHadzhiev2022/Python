import pytest
from playwright.sync_api import *



@pytest.fixture
def api_context(playwright:Playwright) -> APIRequestContext:
    api_context = playwright.request.new_context(base_url="https://dummyjson.com")
    yield api_context
    api_context.dispose()


def test_search_user(api_context: APIRequestContext):
    query = "John"
    response = api_context.get(f"/users/search?q={query}")
    assert response.status == 200

    user_data = response.json()
    assert len(user_data) > 0

    print(f"foundsssssssssssssssssssssssssssssssssssssssssssssssssssssss", user_data["total"])
    print(f"user todatalaaaa: {user_data["total"]}")

