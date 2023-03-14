import pytest
import allure

from page_objects.components.header import HeaderComponent
from page_objects.register_page import RegisterPage
from text_resources.register_constants import RegisterConstants
from test_data.users import RegisterUsersData


@allure.epic('Account Management')
@allure.story('Register Module')
class TestRegister:
    @pytest.fixture(scope='function', autouse=True)
    def before_test(self, driver):
        self.header = HeaderComponent(driver)
        self.register_pg = RegisterPage(driver)
        
    @pytest.mark.high
    @pytest.mark.positive
    def test_register_account_when_all_required_fields_are_fullfill_should_be_successfully(self):
        self.header.when_not_logged_in()
        self.header.open_register_page()
        self.register_pg.expect_page_heading('Register')
        self.register_pg.fill_in_register_form(RegisterUsersData.required_fields_are_fullfill())
        self.register_pg.click_register_btn()
        self.register_pg.expect_url('https://demo.nopcommerce.com/registerresult/1?returnUrl=/')
        self.register_pg.expect_registration_result('Your registration completed')

    @pytest.mark.high
    @pytest.mark.positive
    def test_register_account_when_all_fields_are_fullfill_should_be_successfully(self):
        self.header.when_not_logged_in()
        self.header.open_register_page()
        self.register_pg.expect_page_heading('Register')
        self.register_pg.fill_in_register_form(RegisterUsersData.all_fields_are_fullfill())
        self.register_pg.click_register_btn()
        self.register_pg.expect_registration_result('Your registration completed')

    @pytest.mark.medium
    @pytest.mark.negative
    def test_register_account_should_fail_when_password_and_confirm_pass_are_not_match(self):
        self.header.when_not_logged_in()
        self.header.open_register_page()
        self.register_pg.expect_page_heading('Register')
        self.register_pg.fill_in_register_form(RegisterUsersData.no_match_password())
        self.register_pg.click_register_btn()
        self.register_pg.expect_confirm_pass_error_msg(RegisterConstants.NOT_MATCH_PASSWORD)

    @pytest.mark.medium
    @pytest.mark.negative
    def test_register_account_should_fail_when_email_is_invalid_format(self):
        self.header.when_not_logged_in()
        self.header.open_register_page()
        self.register_pg.expect_page_heading('Register')
        self.register_pg.fill_in_register_form(RegisterUsersData.invalid_email_format())
        self.register_pg.click_register_btn()
        self.register_pg.expect_email_error_msg(RegisterConstants.INVALID_EMAIL_FORMAT)

    @pytest.mark.medium
    @pytest.mark.negative
    def test_register_account_should_fail_when_password_is_less_than_6_chars(self):
        self.header.when_not_logged_in()
        self.header.open_register_page()
        self.register_pg.expect_page_heading('Register')
        self.register_pg.fill_in_register_form(RegisterUsersData.invalid_min_lenth_password())
        self.register_pg.click_register_btn()
        self.register_pg.expect_password_error_msg(RegisterConstants.PASSWORD_RULES)

    @pytest.mark.low
    @pytest.mark.negative
    def test_register_account_should_fail_when_all_required_fields_are_empty(self):
        self.header.when_not_logged_in()
        self.header.open_register_page()
        self.register_pg.expect_page_heading('Register')
        self.register_pg.click_register_btn()
        self.register_pg.expect_first_name_error_msg(RegisterConstants.REQUIRED_FIRST_NAME)
        self.register_pg.expect_last_name_error_msg(RegisterConstants.REQUIRED_LAST_NAME)
        self.register_pg.expect_email_error_msg(RegisterConstants.REQUIRED_EMAIL)
        self.register_pg.expect_password_error_msg(RegisterConstants.REQUIRED_PASSWORD)
        self.register_pg.expect_confirm_pass_error_msg(RegisterConstants.REQUIRED_PASSWORD)