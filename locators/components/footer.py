from selenium.webdriver.common.by import By


class FooterLocators:
    _FOOTER = (By.CSS_SELECTOR, 'div.footer')
    _LINK = (By.TAG_NAME, 'a')
    _IMAGE = (By.TAG_NAME, 'img')