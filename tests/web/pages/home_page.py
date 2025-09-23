from tests.web.pages.base_page import BasePage


class HomePage(BasePage):
    HERO_LOCATOR = "header"  # Simplified, adjust if needed

    def is_hero_visible(self):
        return self.page.is_visible(self.HERO_LOCATOR)
