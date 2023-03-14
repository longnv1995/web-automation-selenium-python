from locators.register_page import RegisterPageLocators
from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._register_pg_locs = RegisterPageLocators
    
    # Locators
    @property
    def page_heading_loc(self):
        return self._register_pg_locs._PAGE_TITLE
    
    @property
    def male_loc(self):
        return self._register_pg_locs._GENDER_MALE
    
    @property
    def female_loc(self):
        return self._register_pg_locs._GENDER_FEMALE
    
    @property
    def fname_loc(self):
        return self._register_pg_locs._FIRST_NAME_FIELD
    
    @property
    def fname_error_loc(self):
        return self._register_pg_locs._FIRST_NAME_ERROR
    
    @property
    def lname_loc(self):
        return self._register_pg_locs._LAST_NAME_FIELD
    
    @property
    def lname_error_loc(self):
        return self._register_pg_locs._LAST_NAME_ERROR
    
    @property
    def dob_day_loc(self):
        return self._register_pg_locs._DOB_DAY
    
    @property
    def dob_month_loc(self):
        return self._register_pg_locs._DOB_MONTH
    
    @property
    def dob_year_loc(self):
        return self._register_pg_locs._DOB_YEAR
    
    @property
    def company_loc(self):
        return self._register_pg_locs._COMPANY_FIELD
    
    @property
    def email_loc(self):
        return self._register_pg_locs._EMAIL_FIELD
    
    @property
    def email_error_loc(self):
        return self._register_pg_locs._EMAIL_ERROR
    
    @property
    def password_loc(self):
        return self._register_pg_locs._PASSWORD_FIELD
    
    @property
    def password_error_loc(self):
        return self._register_pg_locs._PASSWORD_ERROR
    
    @property
    def confirm_pass_loc(self):
        return self._register_pg_locs._CONFIRM_PASSWORD_FIELD
    
    @property
    def confirm_pass_error_loc(self):
        return self._register_pg_locs._CONFIRM_PASSWORD_ERROR
    
    @property
    def register_loc(self):
        return self._register_pg_locs._REGISTER_BTN
    
    @property
    def registration_result_loc(self):
        return self._register_pg_locs._REGISTRATION_RESULT
    
    # Selectors
    def page_heading_txt(self):
        return self.wait_for_text(self.page_heading_loc)
    
    def select_male(self):
        return self.click(self.male_loc)
    
    def select_female(self):
        return self.click(self.female_loc)
    
    def first_name(self):
        return self.find_element(self.fname_loc)
    
    def fist_name_error_msg(self):
        return self.wait_for_text(self.fname_error_loc)

    def last_name(self):
        return self.find_element(self.lname_loc)
    
    def last_name_error_msg(self):
        return self.wait_for_text(self.lname_error_loc)
    
    def email(self):
        return self.find_element(self.email_loc)

    def email_error(self):
        return self.wait_for_text(self.email_error_loc)
    
    def password(self):
        return self.find_element(self.password_loc)
    
    def password_error(self):
        return self.wait_for_text(self.password_error_loc)

    def confirm_pass(self):
        return self.find_element(self.confirm_pass_loc)
    
    def confirm_pass_error(self):
        return self.wait_for_text(self.confirm_pass_error_loc)
    
    def register_btn(self):
        return self.find_element(self.register_loc)
    
    def registration_result(self):
        return self.wait_for_text(self.registration_result_loc)
    
    # Actions
    def click_register_btn(self):
        self.wait_for_click(self.register_loc)

    def enter_first_name(self, text):
        self.enter_text(self.fname_loc, text)
    
    def enter_last_name(self, text):
        self.enter_text(self.lname_loc, text)

    def enter_email(self, text):
        self.enter_text(self.email_loc, text)

    def enter_company_name(self, text):
        self.enter_text(self.company_loc, text)
    
    def enter_password(self, text):
        self.enter_text(self.password_loc, text)

    def enter_confirm_pass(self, text):
        self.enter_text(self.confirm_pass_loc, text)


    # Methods
    def fill_in_register_form(self, user):
        _keys = list(user.keys())
        if 'gender' in _keys:
            if user['gender'].lower() == 'male':
                self.select_male()
            else:
                self.select_female()

        if 'first_name' in _keys:
            self.enter_first_name(user['first_name'])
        
        if 'last_name' in _keys:
            self.enter_last_name(user['last_name'])

        if 'dob_day' in _keys:
            self.select_by_value(self.dob_day_loc, user['dob_day'])

        if 'dob_month' in _keys:
            self.select_by_value(self.dob_month_loc, user['dob_month'])

        if 'dob_year' in _keys:
            self.select_by_value(self.dob_year_loc, user['dob_year'])

        if 'email' in _keys:
            self.enter_email(user['email'])

        if 'company_name' in _keys:
            self.enter_company_name(user['company_name'])

        if 'password' in _keys:
            self.enter_password(user['password'])
        
        if 'confirm_pass' in _keys:
            self.enter_confirm_pass(user['confirm_pass'])

    def expect_first_name_error_msg(self, msg):
        self.verify(self.fist_name_error_msg(), msg)

    def expect_last_name_error_msg(self, msg):
        self.verify(self.last_name_error_msg(), msg)

    def expect_email_error_msg(self, msg):
        self.verify(self.email_error(), msg)

    def expect_password_error_msg(self, msg):
        self.verify(self.password_error(), msg)

    def expect_confirm_pass_error_msg(self, msg):
        self.verify(self.confirm_pass_error(), msg)
    
    def expect_registration_result(self, msg):
        self.verify(self.registration_result(), msg)
    
    def expect_page_heading(self, text):
        self.verify(self.page_heading_txt(), text)


