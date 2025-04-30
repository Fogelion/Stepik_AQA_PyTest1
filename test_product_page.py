# pytest -v --tb=line --language=en test_product_page.py

from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import pytest


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_products_to_cart(browser, link):
#     link = link
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_not_be_success_message()
#     product_page.should_be_cart_button()
#     product_page.add_product_to_cart()
#     product_page.should_be_same_book_name()
#     product_page.should_be_same_book_price()

# def test_guest_can_add_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_not_be_success_message()
#     product_page.should_be_cart_button()
#     product_page.add_product_to_cart()
#     product_page.should_be_same_book_name()
#     product_page.should_be_same_book_price()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    product_page = BasePage(browser, link)
    product_page.open()
    product_page.go_to_login_page()

    # проверка страницы логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# @pytest.mark.xfail(reason="Сообщение об успехе должно появляться после добавления в корзину")
# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_cart_button()
#     product_page.add_product_to_cart()
#     product_page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_not_be_success_message()
#
# @pytest.mark.xfail(reason="Сообщение об успехе не должно пропадать")
# def test_message_disappeared_after_adding_product_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_cart_button()
#     product_page.add_product_to_cart()
#     product_page.should_be_disappeared_success_message()