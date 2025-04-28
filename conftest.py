import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Функция pytest_addoption(parser) — это специальный хук в pytest, который позволяет добавлять кастомные аргументы
# командной строки для ваших тестов. Она работает как "регистратор" новых опций, которые затем можно использовать
# при запуске тестов. Pytest автоматически вызывает эту функцию при запуске, передавая ей объект parser
def pytest_addoption(parser):
    parser.addoption(
        "--language",          # Имя аргумента (как оно будет в командной строке)
        action="store",       # Сохранить переданное значение
        default="en",        # Значение по умолчанию
        help="Set browser language"  # Описание (выводится в --help)
    )
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="session")
def browser(request):
    # Получаем значение --language из командной строки
    user_language = request.config.getoption("language")

    # Настраиваем браузер с выбранным языком
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})

    browser = webdriver.Chrome(options=options)
    print(f"\nstart browser with language: {user_language}")
    yield browser
    print("\nquit browser..")
    browser.quit()