import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

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
    if browser == 'chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.page_load_strategy = 'normal' # none,eager, default='normal'
        # service = ChromeService(executable_path='drivers/chromedriver.exe')
        _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) # -> take longer to run (need to investigate more)
        # _driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError('Not supported browser')
    
    if url:
        _driver.get(url)
    else:
        _driver.get('https://demo.nopcommerce.com/')

    _driver.maximize_window()
    yield _driver

    _driver.close()
    _driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Type in browser type: chrome, firefox')
    parser.addoption('--url', action='store', help='Type url to run automation test')
    parser.addoption('--headless', action='store', help='Run in headless mode (without opening browser)')




