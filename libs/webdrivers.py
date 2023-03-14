from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from utils.custom_enums import SupportedBrowsers, PageLoadStrategy


CHROME_PATH = 'drivers/chromedriver.exe'
FIREFOX_PATH = ''


class WebDriverFactory:
    def __init__(self, browser):
        self._browser = self._init_driver(browser)

    def _init_driver(self, browser):
        _browser = browser.lower()
        if _browser == SupportedBrowsers.CHROME:
            return self.chrome_driver()
        elif _browser == SupportedBrowsers.FIREFOX:
            return self.firefox_driver()
        else:
            raise ValueError(f'No supported browser! {_browser}')

    def chrome_driver(self):
        options = ChromeOptions()
        options.page_load_strategy = 'none'
        service = ChromeService(executable_path=CHROME_PATH)
        _driver = webdriver.Chrome(service=service, options=options)

        return _driver

    def firefox_driver(self):
        options = FirefoxOptions()
        firefox_profile = FirefoxProfile()
        service = ChromeService(executable_path=CHROME_PATH)
        firefox_profile.set_preference("javascript.enabled", False)
        options.profile = firefox_profile
        _driver = webdriver.Chrome(service=service, options=options)

        return _driver