from selenium.webdriver.common.by import By

class MainPageLocators():
    # теперь каждый селектор — это пара: как искать и что искать
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")