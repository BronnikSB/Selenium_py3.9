from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


# Добавляем параметр командной строки
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language: ec or fr')


# Фикстура: Запустить браузер
@pytest.fixture(scope='function')
def browser(request):
    # Запрос значения параметра
    languages = request.config.getoption('language')

    option = Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': languages})

    browser = webdriver.Chrome(options=option)
    browser.maximize_window()
    yield browser
    print('/n quit browser...')
    browser.quit()
