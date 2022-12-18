import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(6)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = Options()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(6)
    else:
        raise pytest.UsageError("check Syntax")
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()