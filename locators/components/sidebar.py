from selenium.webdriver.common.by import By


class SidebarLocators:
    _SIDEBAR = (By.CSS_SELECTOR, 'div.side-2')
    _LINK = (By.TAG_NAME, 'a')
    _IMAGE = (By.TAG_NAME, 'img')