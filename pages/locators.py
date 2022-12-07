from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN = (By.ID, "id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    PASSWORD_SUBMIT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRICE = (By.CSS_SELECTOR, "div.product_main > p")
    ADD_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    TITLE = (By.CSS_SELECTOR, "div.product_main > h1")
    ADD_TITLE = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOOK_BASKET = (By.CSS_SELECTOR, "span > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    PRODUCT_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY = (By.CSS_SELECTOR, "#content_inner p")