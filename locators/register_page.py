from selenium.webdriver.common.by import By


class RegisterPageLocators:
    _PAGE_TITLE = (By.CSS_SELECTOR, 'div.page-title > h1')
    _GENDER_MALE = (By.ID, 'gender-male')
    _GENDER_FEMALE = (By.ID, 'gender-female')
    _FIRST_NAME_FIELD = (By.ID, 'FirstName')
    _FIRST_NAME_ERROR = (By.ID, 'FirstName-error')
    _LAST_NAME_FIELD = (By.ID, 'LastName')
    _LAST_NAME_ERROR = (By.ID, 'LastName-error')
    _DOB_DAY = (By.NAME, 'DateOfBirthDay')
    _DOB_MONTH = (By.NAME, 'DateOfBirthMonth')
    _DOB_YEAR = (By.NAME, 'DateOfBirthYear')
    _EMAIL_FIELD = (By.ID, 'Email')
    _EMAIL_ERROR = (By.ID, 'Email-error')
    _COMPANY_FIELD = (By.ID, 'Company')
    _PASSWORD_FIELD = (By.ID, 'Password')
    _PASSWORD_ERROR = (By.ID, 'Password-error')
    _CONFIRM_PASSWORD_FIELD = (By.ID, 'ConfirmPassword')
    _CONFIRM_PASSWORD_ERROR = (By.ID, 'ConfirmPassword-error')
    _REGISTER_BTN = (By.ID, 'register-button')
    _REGISTRATION_RESULT = (By.CLASS_NAME, 'result')