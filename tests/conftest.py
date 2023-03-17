import pytest
import os

from libs.webdrivers import WebDriverFactory
from utils.helpers import load_env_file


load_env_file()
BASE_URL = os.getenv('DEV_BASE_URL')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption('--url')

@pytest.fixture(scope='session')
def headless(request):
    return request.config.getoption('--headless')

# Init driver
@pytest.fixture(scope='function')
def driver(browser, url, headless):
    browser = browser.lower()
    wdf = WebDriverFactory(browser, headless)
    _driver = wdf._init_driver()
    if url:
        _driver.get(url)
    else:
        _driver.get(BASE_URL)

    _driver.maximize_window()
    yield _driver

    _driver.close()
    _driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Type in browser type: chrome, firefox')
    parser.addoption('--url', action='store', help='Type url to run automation test')
    parser.addoption('--headless', action='store', help='Run in headless mode (without opening browser)')




