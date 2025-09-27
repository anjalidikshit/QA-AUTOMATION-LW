import pytest
from playwright.async_api import async_playwright


@pytest.fixture(scope="session")
async def browser():
    """Launch a single browser for the session (async)."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, slow_mo=50)
        yield browser
        await browser.close()


@pytest.fixture(scope="function")
async def page(browser):
    """Fresh browser page for each test (async)."""
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()
