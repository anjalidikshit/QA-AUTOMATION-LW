import pytest
from utils import config, logger
from tests.web.pages.home_page import HomePage

log = logger.get_logger(__name__)


@pytest.mark.parametrize("url", [config.BASE_URL])
def test_homepage_loads(page, url):
    log.info(f"Navigating to {url}")
    homepage = HomePage(page)
    homepage.visit(url)

    log.info("Checking page title")
    title = homepage.get_title()
    assert "Latham & Watkins" in title, f"Unexpected title: {title}"

    log.info("Checking hero section visibility")
    assert homepage.is_hero_visible(), "Hero section not visible"

    log.info("Homepage test completed successfully.")
