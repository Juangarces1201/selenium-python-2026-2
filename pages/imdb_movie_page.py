
from selenium.webdriver.common.by import By
from .base_page import BasePage


class IMDbMoviePage(BasePage):
    RATING = (
        By.CSS_SELECTOR,
        '[data-testid="hero-rating-bar__aggregate-rating__score"] span'
    )

    def get_rating(self):
        return self.find_element(self.RATING).text
