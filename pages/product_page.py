from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_correct_information(self):
        self.should_be_correct_price()
        self.should_be_correct_name()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "There is no 'Add to basket' button on the page"

    def should_be_correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        add_price = self.browser.find_element(*ProductPageLocators.ADD_PRICE).text
        assert price == add_price, "Price is not correct"

    def should_be_correct_name(self):
        title = self.browser.find_element(*ProductPageLocators.TITLE).text
        add_title = self.browser.find_element(*ProductPageLocators.ADD_TITLE).text
        assert title == add_title, "Title is not correct"
    def should_not_be_success_message_after_adding(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There is no success message on the page after adding"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There is no success message on the page"

    def should_dissapear_after_adding(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message has not dissappered"

