from locators.components.header import HeaderLocators
from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage
from test_data.users import UsersData


class HeaderComponent(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._header_locs = HeaderLocators
        self._login = LoginPage(driver)

    # Locators
    @property
    def header_loc(self):
        return self._header_locs._HEADER
    
    @property
    def link_loc(self):
        return self._header_locs._LINK
    
    @property
    def image_loc(self):
        return self._header_locs._IMAGE
    
    @property
    def menu_loc(self):
        return self._header_locs._MENU
    
    @property
    def register_loc(self):
        return self._header_locs._REGISTER_LINK
    
    @property
    def login_loc(self):
        return self._header_locs._LOGIN_LINK
    
    @property
    def logout_loc(self):
        return self._header_locs._LOGOUT_LINK
    
    @property
    def account_loc(self):
        return self._header_locs._ACCOUNT_LINK

    @property
    def wishlist_loc(self):
        return self._header_locs._WISHLIST_LINK
    
    @property
    def cart_loc(self):
        return self._header_locs._CART_LINK
    
    @property
    def cart_qty_loc(self):
        return self._header_locs._CART_QTY
    
    # Actions
    def open_register_page(self):
        self.wait_for_click(self.register_loc)

    def open_login_page(self):
        self.wait_for_click(self.login_loc)

    def open_wishlist_page(self):
        self.wait_for_click(self.wishlist_loc)

    def hover_over_cart(self):
        pass

    def click_logout(self):
        return self.wait_for_click(self.logout_loc)
    
    
    # Selectors
    def cart_qty(self):
        return self.wait_for_text(self.cart_qty_loc)

    # Methods
    def when_not_logged_in(self):
        is_login_visible = self.wait_for_visible(self.login_loc)
        self.assert_true(is_login_visible)

    def when_logged_in_as_user(self):
        self.when_not_logged_in()
        self.navigate_to('/login')
        self._login.expect_page_heading('Welcome, Please Sign In!')
        self._login.fill_in_login_form(UsersData.valid_user())
        self._login.click_login_btn()
        self.expect_logout_is_displayed()

    def expect_login_is_disappeared(self):
        is_login_disappeared = self.wait_for_disappeared(self.login_loc)
        self.assert_true(is_login_disappeared)

    def expect_login_is_displayed(self):
        is_login_displayed = self.wait_for_visible(self.login_loc)
        self.assert_true(is_login_displayed)

    def expect_register_is_disappeared(self):
        is_register_disappeared = self.wait_for_disappeared(self.register_loc)
        self.assert_true(is_register_disappeared)

    def expect_logout_is_displayed(self):
        is_log_out_displayed = self.wait_for_visible(self.logout_loc)
        self.assert_true(is_log_out_displayed)

    def expect_account_is_displayed(self):
        is_account_displayed = self.wait_for_visible(self.account_loc)
        self.assert_true(is_account_displayed)

    def find_links_in_header(self) -> list:
        return self.find_links_from(self.link_loc, self.header_loc) 

    def find_links_in_menu(self) -> list:
        return self.find_links_from(self.link_loc, self.menu_loc)    
    
    def find_images_in_header(self) -> list:
        return self.find_images_from(self.image_loc, self.header_loc) 

    def find_images_in_menu(self) -> list:
        return self.find_images_from(self.image_loc, self.menu_loc)    