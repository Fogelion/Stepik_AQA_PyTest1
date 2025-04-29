from .base_page import BasePage
from .locators import ProductPageLocators
import re
import time


class ProductPage(BasePage):
    total_books_price = 0

    def add_product_to_cart(self):
        cart_add = self.browser.find_element(*ProductPageLocators.CART_ADD)
        cart_add.click()
        self.solve_quiz_and_get_code()
        # time.sleep(1)

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.CART_ADD), "Cart button is not presented"

    def should_be_same_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        print(f"Название книги: {book_name.text}")
        book_name_add = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADD)
        print(f"Название книги в корзине: {book_name_add.text}")
        assert book_name.text == book_name_add.text, "Book name not equal to cart book name"

    def should_be_same_book_price(self):
        book_price_elem = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = round(float(book_price_elem.text[1:]), 2)
        print(f"Цена книги: £{book_price}")
        ProductPage.total_books_price += book_price
        print(f"Текущая сумма всех книг: £{ProductPage.total_books_price}")
        cart_price_elem = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        cart_price = float(re.search(r'[\d,]+\.\d{2}', cart_price_elem.text).group())
        print(f"Стоимость корзины: £{cart_price}")
        assert abs(cart_price - ProductPage.total_books_price) < 0.01, \
                f"Cart price {cart_price} not equal to total books price {self.total_books_price}"