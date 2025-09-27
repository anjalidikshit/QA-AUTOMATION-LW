from .base_page import BasePage
from utils import config

class HomePage(BasePage):
    HERO_LOCATOR = "section.hero"

    async def visit(self, url=config.BASE_URL):
        await self.page.goto(url)

    async def open(self):
        # wrapper for visit(), defaults to BASE_URL
        await self.visit(config.BASE_URL)

    async def get_title(self):
        return await self.page.title()

    async def is_hero_visible(self):
        return await self.page.is_visible(self.HERO_LOCATOR, timeout=5000)
