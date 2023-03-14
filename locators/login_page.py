from selenium.webdriver.common.by import By


class LoginPageLocators:
    _PAGE_TITLE = (By.CSS_SELECTOR, 'div.page-title > h1')
    _EMAIL_FIELD = (By.ID, 'Email')
    _EMAIL_ERROR = (By.ID, 'Email-error')
    _PASSWORD_FIELD = (By.ID, 'Password')
    _LOGIN_BTN = (By.CLASS_NAME, 'login-button')
    _LOGIN_ERROR = (By.CLASS_NAME, 'validation-summary-errors')
    _REGISTER_BTN = (By.CSS_SELECTOR, 'button.register-button')
    _CHECKOUT_AS_GUEST_BTN = (By.CSS_SELECTOR, 'button.checkout-as-guest-button')