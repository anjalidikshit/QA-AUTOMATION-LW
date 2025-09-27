# home_page.py
from tests.web.pages.base_page import BasePage

class HomePage(BasePage):
    HERO_LOCATOR = "header"

    async def is_hero_visible(self):
        return await self.page.is_visible(self.HERO_LOCATOR)
