from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language (e.g. en, es, fr)"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=profile)
    else:
        raise pytest.UsageError("--browser option should be chrome or firefox")
    yield browser
    browser.quit()