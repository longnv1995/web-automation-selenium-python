from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.custom_enums import SupportedBrowsers, PageLoadStrategy


class WebDriverFactory:
    def __init__(self, browser, headless=False):
        self._browser = browser
        self._headless = headless

    def _init_driver(self):
        _browser = self._browser.lower()
        if _browser == SupportedBrowsers.CHROME:
            return self.chrome_driver()
        elif _browser == SupportedBrowsers.FIREFOX:
            return self.firefox_driver()
        else:
            raise ValueError(f'No supported browser! {_browser}')

    def chrome_driver(self):
        options = ChromeOptions()
        if self._headless:
            options.add_argument('--headless')
        options.page_load_strategy = PageLoadStrategy.NONE
        _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        return _driver

    def firefox_driver(self):
        options = FirefoxOptions()
        if self._headless:
            options.add_argument('--headless')
        options.page_load_strategy = PageLoadStrategy.NONE
        _driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

        return _driver