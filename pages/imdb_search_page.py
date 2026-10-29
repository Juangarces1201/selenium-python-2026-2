
from selenium.webdriver.common.by import By
from .base_page import BasePage


class IMDbSearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "suggestion-search")
    FIRST_RESULT = (By.CSS_SELECTOR, ".searchResult__constTitle")

    def search(self, title):
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(title)

    def open_first_result(self):
        self.click(self.FIRST_RESULT)
