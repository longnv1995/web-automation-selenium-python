from locators.login_page import LoginPageLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._login_pg_locs = LoginPageLocators

    # Locators
    @property
    def page_heading_loc(self):
        return self._login_pg_locs._PAGE_TITLE
         
    @property
    def email_loc(self):
        return self._login_pg_locs._EMAIL_FIELD
    
    @property
    def email_error_loc(self):
        return self._login_pg_locs._EMAIL_ERROR
    
    @property
    def password_loc(self):
        return self._login_pg_locs._PASSWORD_FIELD
    
    @property
    def login_error_loc(self):
        return self._login_pg_locs._LOGIN_ERROR
    
    @property
    def login_loc(self):
        return self._login_pg_locs._LOGIN_BTN
    
    @property
    def checkout_as_guest_loc(self):
        return self._login_pg_locs._CHECKOUT_AS_GUEST_BTN
    
    @property
    def register_loc(self):
        return self._login_pg_locs._REGISTER_BTN
    
    # Selectors
    def page_heading_txt(self):
        return self.wait_for_text(self.page_heading_loc)
    
    def email(self):
        return self.find_element(self.email_loc)

    def email_error(self):
        return self.wait_for_text(self.email_error_loc)
    
    def password(self):
        return self.find_element(self.password_loc)
    
    def login_error(self):
        return self.wait_for_text(self.login_error_loc)
    
    def checkout_as_guest(self):
        return self.wait_for_element(self.checkout_as_guest_loc)
    
    def register_btn(self):
        return self.wait_for_element(self.register_loc)
    
    # Actions
    def click_login_btn(self):
        self.wait_for_click(self.login_loc)

    def enter_email(self, text):
        self.enter_text(self.email_loc, text)

    def enter_password(self, text):
        self.enter_text(self.password_loc, text)

    def click_checkout_as_guest_btn(self):
        self.wait_for_click(self.checkout_as_guest_loc)

    def click_register_btn(self):
        self.wait_for_click(self.register_loc)

    # Methods
    def fill_in_login_form(self, user):
        self.enter_email(user['email'])
        self.enter_password(user['password'])

    def login(self, user):
        self.fill_in_login_form(user)
        self.click_login_btn()

    def expect_email_error_msg(self, msg):
        self.verify(self.email_error(), msg)

    def expect_login_error_msg(self, msg):
        self.verify(self.login_error(), msg)

    def expect_page_heading(self, text):
        self.verify(self.page_heading_txt(), text)


