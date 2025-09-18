import pytest
from playwright.sync_api import sync_playwright
from tests.web.pages.home_page import HomePage

@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

def test_search_ai(setup):
    page = setup
    home = HomePage(page)
    home.open()
    home.click_search()
    home.enter_search_term("AI")
    page.wait_for_selector(".SearchResults")
    assert "AI" in page.inner_text(".SearchResults")
