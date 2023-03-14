import pytest
import allure

from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage
from page_objects.components.header import HeaderComponent
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage
from text_resources.product_constants import ProductConstants
from test_data.products import ProductsData
from test_data.orders import OrdersData


@allure.epic('Order Management')
@allure.story('Checkout Module')
class TestOrderProduct:
    @pytest.fixture(scope='function', autouse=True)
    def before_test(self, driver):
        self.header = HeaderComponent(driver)
        self.product_pg = ProductPage(driver)
        self.login_pg = LoginPage(driver)
        self.cart_pg = CartPage(driver)
        self.checkout_pg = CheckoutPage(driver)

    @pytest.mark.high
    @pytest.mark.positive
    def test_order_one_product_should_be_successfully_when_checkout_as_guest(self):
        product = ProductsData.new_price_book()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(1)
        self.cart_pg.check_agree_terms()
        self.cart_pg.click_checkout_btn()
        self.login_pg.click_checkout_as_guest_btn()
        self.checkout_pg.fill_in_billing_form_and_continue(OrdersData.full_billing_fields())
        self.checkout_pg.select_shipping_method_and_continue()
        self.checkout_pg.select_payment_method_and_continue()
        self.checkout_pg.check_payment_info_and_continue()
        self.checkout_pg.confirm_order()
        self.checkout_pg.expect_order_completed_title('Your order has been successfully processed!')
        self.checkout_pg.expect_url('https://demo.nopcommerce.com/checkout/completed')
        self.checkout_pg.view_order_details()

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('product1, product2', 
        [
            (ProductsData.basic_belt(), ProductsData.new_price_and_free_shipping_book())
        ]
    )
    def test_order_two_products_should_be_successfully_when_checkout_as_guest(self, product1, product2):
        self.header.when_not_logged_in()
        self.header.view_product(product1)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.view_product(product2)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(2)
        self.cart_pg.check_agree_terms()
        self.cart_pg.click_checkout_btn()
        self.login_pg.click_checkout_as_guest_btn()
        self.checkout_pg.fill_in_billing_form_and_continue(OrdersData.required_billing_fields())
        self.checkout_pg.select_shipping_method_and_continue()
        self.checkout_pg.select_payment_method_and_continue()
        self.checkout_pg.check_payment_info_and_continue()
        self.checkout_pg.confirm_order()
        self.checkout_pg.view_order_details()
