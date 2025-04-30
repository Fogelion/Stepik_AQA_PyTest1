from selenium.webdriver.common.by import By

class BasePageLocators():
    # теперь каждый селектор — это пара: как искать и что искать
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    CART_ADD = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.CSS_SELECTOR, "#content_inner > article > div > div.product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div > div.product_main > p.price_color")
    CART_PRICE = (By.CSS_SELECTOR, "div.page_inner > div > div.basket-mini")
    BOOK_NAME_ADD = (By.CSS_SELECTOR, "#messages > div:first-child > .alertinner > strong")