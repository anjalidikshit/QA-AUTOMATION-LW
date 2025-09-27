# base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page

    async def visit(self, url: str):
        await self.page.goto(url)

    async def get_title(self):
        return await self.page.title()
