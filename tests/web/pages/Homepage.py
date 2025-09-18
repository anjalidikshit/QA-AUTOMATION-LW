from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_BUTTON = "button[aria-label='Search']"
    SEARCH_INPUT = "input[type='search']"

    def open(self):
        self.navigate("https://www.lw.com")

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def enter_search_term(self, term: str):
        self.fill(self.SEARCH_INPUT, term)
        self.page.keyboard.press("Enter")