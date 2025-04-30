# pytest -v --tb=line --language=en test_main_page.py

from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    # Проверить, что есть ссылка, которая ведет на логин
    page.should_be_login_link()
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

    # проверка страницы логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
