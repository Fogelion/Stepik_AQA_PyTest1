# pytest -v --tb=line --language=en test_product_page.py

# Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром -s:
# pytest -s test_foo.py

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_cart_button()
    product_page.add_product_to_cart()
    product_page.should_be_same_book_name()
    product_page.should_be_same_book_price()