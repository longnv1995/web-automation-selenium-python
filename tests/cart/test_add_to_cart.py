import pytest
import allure

from page_objects.components.header import HeaderComponent
from page_objects.product_page import ProductPage
from text_resources.product_constants import ProductConstants
from test_data.products import ProductsData


@allure.epic('Order Management')
@allure.story('Cart Module')
class TestAddProductToCart:
    @pytest.fixture(scope='function', autouse=True)
    def before_test(self, driver):
        self.header = HeaderComponent(driver)
        self.product_pg = ProductPage(driver)

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('product', 
        [
            ProductsData.new_price_book(),
            ProductsData.new_price_and_free_shipping_book(),
            ProductsData.basic_belt(),
            ProductsData.basic_sunglass()
        ],
        ids = ['book has new price', 'book has new price and free shipping', 'belt product', 'sunglass']
    )
    def test_add_different_basic_book_type_to_cart_should_be_successfully_when_not_logged_in(self, product):
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.verify_product_details(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.expect_cart_qty(1)

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('qty', [1, 2])
    def test_add_free_shipping_book_to_cart_with_different_qty_should_be_successfully_when_not_logged_in(self, qty):
        product = ProductsData.new_price_and_free_shipping_book()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.verify_product_details(product)
        self.product_pg.add_qty(qty)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.expect_cart_qty(qty)

    @pytest.mark.medium
    @pytest.mark.positive
    def test_add_product_to_cart_should_be_successfully_when_add_invalid_qty_and_then_valid_qty(self):
        product = ProductsData.shoe_with_size_and_color()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.expect_product_name(product)
        self.product_pg.add_qty(-1)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_add_to_cart_failed(ProductConstants.INVALID_QTY)

    @pytest.mark.high
    @pytest.mark.positive
    def test_add_basic_hat_to_cart_should_be_successfully_when_not_logged_in(self):
        product = ProductsData.basic_hat()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.expect_product_name(product)
        self.product_pg.select_size('Medium')
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.expect_cart_qty(1)

    @pytest.mark.high
    @pytest.mark.positive
    def test_add_notebook_min_qty_2_to_cart_should_be_successfully_when_not_logged_in(self):
        product = ProductsData.notebook_min_qty_2()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.verify_product_details(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.expect_cart_qty(2)

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('product1, product2', 
        [
            (ProductsData.basic_belt(), ProductsData.new_price_and_free_shipping_book())
        ]
    )
    def test_add_two_products_to_cart_should_be_successfully_when_not_logged_in(self, product1, product2):
        self.header.when_not_logged_in()
        self.header.view_product(product1)
        self.product_pg.expect_product_name(product1)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.view_product(product2)
        self.product_pg.expect_product_name(product2)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_added_to_cart_successfully(ProductConstants.ADDED_TO_CART_SUCCESSFULLY)
        self.product_pg.expect_cart_qty(2)
    
    @pytest.mark.medium
    @pytest.mark.negative
    def test_add_notebook_min_qty_2_to_cart_with_qty_less_than_minimum_qty_should_fail_when_not_logged_in(self):
        product = ProductsData.notebook_min_qty_2()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.verify_product_details(product)
        self.product_pg.add_qty(1)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_add_to_cart_failed(ProductConstants.MINIMUM_QTY)

    @pytest.mark.medium
    @pytest.mark.negative
    def test_add_product_to_cart_with_exceeds_max_qty_should_fail_when_not_logged_in(self):
        product = ProductsData.new_price_book()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.verify_product_details(product)
        self.product_pg.add_qty(10001)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_add_to_cart_failed(ProductConstants.EXCEEDED_MAX_QTY)

    @pytest.mark.medium
    @pytest.mark.negative
    def test_add_shoe_with_size_and_color_to_cart_without_size_should_be_successfully_when_not_logged_in(self):
        product = ProductsData.shoe_with_size_and_color()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.expect_product_name(product)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_add_to_cart_failed(ProductConstants.REQUIRED_SIZE)

    @pytest.mark.medium
    @pytest.mark.negative
    @pytest.mark.parametrize('qty', 
        ['-2', 0, 'str', '@@'],
        ids=['negative number', 'zero', 'not a number', 'invalid character']
    )
    def test_add_free_shipping_book_to_cart_with_invalid_qty_should_be_successfully_when_not_logged_in(self, qty):
        product = ProductsData.new_price_and_free_shipping_book()
        self.header.when_not_logged_in()
        self.header.view_product(product)
        self.product_pg.verify_product_details(product)
        self.product_pg.add_qty(qty)
        self.product_pg.click_add_to_cart_btn()
        self.product_pg.expect_add_to_cart_failed(ProductConstants.INVALID_QTY)