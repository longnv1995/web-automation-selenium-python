from selenium.webdriver.common.by import By


class MainAreaLocators:
    _MAIN_AREA = (By.CSS_SELECTOR, 'div.master-wrapper-content')
    _LINK = (By.TAG_NAME, 'a')
    _IMAGE = (By.TAG_NAME, 'img')