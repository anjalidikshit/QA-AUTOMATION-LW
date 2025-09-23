import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """Launch a single browser for the session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=50)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Fresh browser page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
