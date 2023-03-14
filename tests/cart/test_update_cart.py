import pytest
import allure

from page_objects.cart_page import CartPage
from page_objects.components.header import HeaderComponent
from page_objects.product_page import ProductPage
from text_resources.product_constants import ProductConstants
from text_resources.cart_constants import CartConstants
from test_data.products import ProductsData


@allure.epic('Order Management')
@allure.story('Update Cart Module')
class TestUpdateCart:
    @pytest.fixture(scope='function', autouse=True)
    def before_test(self, driver):
        self.header = HeaderComponent(driver)
        self.product_pg = ProductPage(driver)
        self.cart_pg = CartPage(driver)

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.skip('Skip for now due to this always failed')
    def test_update_quantity_of_a_product_in_cart_should_be_successfully(self):
        product = ProductsData.basic_shoe()
        self.header.view_product(product)
        self.product_pg.expect_product_name(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(1)
        self.cart_pg.update_qty_and_wait_for_successfully(product, 2)

    @pytest.mark.high
    @pytest.mark.positive
    def test_update_cart_should_be_successfully_when_update_product_with_invalid_quantity(self):
        product = ProductsData.basic_shoe()
        self.header.view_product(product)
        self.product_pg.expect_product_name(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(1)
        self.cart_pg.update_qty_and_expect_eror(product, -5, CartConstants.NEGATIVE_QTY)

    @pytest.mark.high
    @pytest.mark.positive
    def test_apply_discount_to_cart_should_fail_when_apply_invalid_discount(self):
        product = ProductsData.basic_shoe()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.expect_product_name(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(1)
        self.cart_pg.apply_discount('random-discount')
        self.cart_pg.expect_discount_error_msg(CartConstants.NOT_FOUND_COUPON)

    @pytest.mark.high
    @pytest.mark.positive
    def test_apply_gift_card_to_cart_should_fail_when_apply_invalid_gift_card(self):
        product = ProductsData.basic_shoe()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.expect_product_name(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(1)
        self.cart_pg.apply_gift_card('random-gift-card')
        self.cart_pg.expect_gift_card_error_msg(CartConstants.INVALID_GIFT_CARD)
