# pytest -v --tb=line --language=en test_main_page.py

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    # Проверить, что есть ссылка, которая ведет на логин
    page.should_be_login_link()
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

    # проверка страницы логина
    login_page_url = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, login_page_url)
    login_page.should_be_login_page()
