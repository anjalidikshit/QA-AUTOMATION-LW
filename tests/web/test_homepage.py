import pytest
from utils import config
from tests.web.pages.home_page import HomePage

@pytest.mark.asyncio
@pytest.mark.parametrize("url", [config.BASE_URL])
async def test_homepage_loads(page, url):
    homepage = HomePage(page)

    await homepage.visit(url)

    title = await homepage.get_title()
    assert "Latham & Watkins" in title, f"Unexpected title: {title}"

    assert await homepage.is_hero_visible(), "Hero section not visible"
