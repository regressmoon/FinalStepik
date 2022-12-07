from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link2 = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link2)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "StepikTest123"
        password_submit = "StepikTest123"
        login_page.register_new_user(email=email, password=password, password_submit=password_submit)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_correct_information()

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_information()

@pytest.mark.xfail(scope="function")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message_after_adding()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(scope="function")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_dissapear_after_adding()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, product_link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_text()
    page.should_not_be_product()