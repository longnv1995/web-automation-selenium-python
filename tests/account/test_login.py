import pytest
import allure

from page_objects.components.header import HeaderComponent
from page_objects.login_page import LoginPage
from page_objects.register_page import RegisterPage
from text_resources.login_constants import LoginConstants
from test_data.users import RegisterUsersData, UsersData


@allure.epic('Account Management')
@allure.story('Login Module')
class TestSignIn:
    @pytest.fixture(scope='function', autouse=True)
    def before_test(self, driver):
        self.header = HeaderComponent(driver)
        self.register_pg = RegisterPage(driver)
        self.login_pg = LoginPage(driver)

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.skip('This test will fail due to this account has been removed from system after a while')
    def test_login_should_be_successfully_when_login_with_valid_email_and_password(self):
        self.header.when_not_logged_in()
        self.header.open_login_page()
        self.login_pg.expect_page_heading('Welcome, Please Sign In!')
        self.login_pg.fill_in_login_form(UsersData.valid_user())
        self.login_pg.click_login_btn()
        # self.login_pg.login(login_users(''))
        self.header.expect_login_is_disappeared()
        self.header.expect_register_is_disappeared()
        self.header.expect_account_is_displayed()
        self.header.expect_logout_is_displayed()
    
    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.skip('This test will fail due to this account has been removed from system after a while')
    def test_logout_should_be_successfully_when_click_log_out(self):
        self.header.when_logged_in_as_user()
        self.header.click_logout()
        self.header.expect_login_is_displayed()

    @pytest.mark.high
    @pytest.mark.positive
    def test_login_should_be_successfully_when_login_with_new_register_account(self):
        create_user_info = RegisterUsersData.required_fields_are_fullfill()
        self.header.when_not_logged_in()
        self.header.open_register_page()
        self.register_pg.expect_page_heading('Register')
        self.register_pg.fill_in_register_form(create_user_info)
        self.register_pg.click_register_btn()
        self.register_pg.expect_registration_result('Your registration completed')
        self.header.open_login_page()
        self.login_pg.fill_in_login_form(create_user_info)
        self.login_pg.click_login_btn()
        self.header.expect_login_is_disappeared()
        self.header.expect_logout_is_displayed()

    @pytest.mark.low
    @pytest.mark.negative
    def test_login_should_failed_when_login_with_non_existing_user(self):
        self.header.when_not_logged_in()
        self.header.open_login_page()
        self.login_pg.expect_page_heading('Welcome, Please Sign In!')
        self.login_pg.fill_in_login_form(UsersData.non_existing_user())
        self.login_pg.click_login_btn()
        # self.login_pg.expect_login_error_msg(LoginConstants.LOGIN_ERROR)

    @pytest.mark.medium
    @pytest.mark.negative
    def test_login_should_failed_when_login_with_correct_email_and_invalid_password(self):
        self.header.when_not_logged_in()
        self.header.open_login_page()
        self.login_pg.expect_page_heading('Welcome, Please Sign In!')
        self.login_pg.fill_in_login_form(UsersData.invalid_password())
        self.login_pg.click_login_btn()
        # self.login_pg.expect_login_error_msg(LoginConstants.LOGIN_ERROR)

    @pytest.mark.medium
    @pytest.mark.negative
    def test_login_should_failed_when_login_with_invalid_email_format(self):
        self.header.when_not_logged_in()
        self.header.open_login_page()
        self.login_pg.expect_page_heading('Welcome, Please Sign In!')
        self.login_pg.fill_in_login_form(UsersData.invalid_email_format())
        self.login_pg.click_login_btn()
        self.login_pg.expect_email_error_msg(LoginConstants.INVALID_EMAIL_FORMAT)
        
    @pytest.mark.medium
    @pytest.mark.negative
    def test_login_should_failed_when_login_with_email_and_password_are_empty(self):
        self.header.when_not_logged_in()
        self.header.open_login_page()
        self.login_pg.expect_page_heading('Welcome, Please Sign In!')
        self.login_pg.click_login_btn()
        self.login_pg.expect_email_error_msg(LoginConstants.REQUIRED_LOGIN_EMAIL)

    