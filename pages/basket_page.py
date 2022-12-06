from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY), "The basket page has not empty text"

    def should_not_be_product(self):
        shopping_text = self.is_not_element_present(*BasketPageLocators.PRODUCT_BASKET), "The basket is not empty"