from selenium.webdriver.common.by import By

class MainPageLocators():
    # теперь каждый селектор — это пара: как искать и что искать
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")