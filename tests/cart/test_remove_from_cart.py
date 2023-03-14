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
    def test_product_no_exist_in_cart_when_remove_product_from_cart(self):
        product = ProductsData.new_price_and_free_shipping_book()
        self.header.view_product(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.expect_cart_qty(1)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(1)
        self.cart_pg.remove_product(product)
        self.cart_pg.expect_empty_cart_msg('Your Shopping Cart is empty!')

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('product1, product2', 
        [
            (ProductsData.basic_belt(), ProductsData.new_price_and_free_shipping_book())
        ]
    )
    def test_cart_shoud_be_empty_when_remove_all_products_from_cart(self, product1, product2):
        self.header.view_product(product1)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.view_product(product2)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(2)
        self.cart_pg.remove_products()
        self.cart_pg.expect_empty_cart_msg('Your Shopping Cart is empty!')

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('product1, product2', 
        [
            (ProductsData.basic_belt(), ProductsData.new_price_and_free_shipping_book())
        ]
    )
    def test_remove_one_of_product_from_cart_should_be_successfully(self, product1, product2):
        self.header.view_product(product1)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.view_product(product2)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.click_link_to_view_cart()
        self.cart_pg.expect_cart_items(2)
        self.cart_pg.remove_product(product1)
        self.cart_pg.expect_cart_items(1)