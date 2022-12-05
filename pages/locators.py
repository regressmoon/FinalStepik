from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRICE = (By.CSS_SELECTOR, "div.product_main > p")
    ADD_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    TITLE = (By.CSS_SELECTOR, "div.product_main > h1")
    ADD_TITLE = (By.CSS_SELECTOR, "div.alertinner > strong")