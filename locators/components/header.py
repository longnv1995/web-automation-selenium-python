from selenium.webdriver.common.by import By


class HeaderLocators:
    _HEADER = (By.CSS_SELECTOR, 'div.header')
    _LINK = (By.TAG_NAME, 'a')
    _IMAGE = (By.TAG_NAME, 'img')
    _MENU = (By.CSS_SELECTOR, 'div.header-menu')
    _REGISTER_LINK = (By.CSS_SELECTOR, 'a.ico-register')
    _LOGIN_LINK = (By.CSS_SELECTOR, 'a.ico-login')
    _LOGOUT_LINK = (By.CSS_SELECTOR, 'a.ico-logout')
    _ACCOUNT_LINK = (By.CSS_SELECTOR, 'a.ico-account')
    _WISHLIST_LINK = (By.CSS_SELECTOR, 'a.ico-wishlist')
    _CART_LINK = (By.CSS_SELECTOR, 'a.ico-cart')
    _CART_QTY = (By.CSS_SELECTOR, 'a.ico-cart > span.cart-qty')

    _SEARCH_BOX = (By.ID, 'small-searchterms')
    _SEARCH_BTN = (By.CSS_SELECTOR, 'button[class="button-1 search-box-button"]')