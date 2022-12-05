import time

from .pages.product_page import ProductPage


def test_guest_can_add_prodect_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_information()