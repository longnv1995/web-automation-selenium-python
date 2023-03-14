import time
import pytest
from page_objects.category_page import CategoryPage

from page_objects.components.header import HeaderComponent
from page_objects.product_page import ProductPage


class TestProducts:
    @pytest.fixture(scope='function', autouse=True)
    def before_test(self, driver):
        self.header = HeaderComponent(driver)
        self.cate_pg = CategoryPage(driver)
        self.product_pg = ProductPage(driver)

    @pytest.mark.high
    @pytest.mark.positive
    def test_products_when_sort_by_name_in_ascending_should_list_products_ordered_by_ascending_name(self):
        self.header.view_category('notebooks')
        self.cate_pg.expect_category_name('Notebooks')
        self.cate_pg.sort_products_by('Name: A to Z')
        self.cate_pg.expect_url_contains('orderby=5')
        self.cate_pg.expect_sorted_product_name_in_ascending()
        
    @pytest.mark.high
    @pytest.mark.positive
    def test_products_when_sort_by_name_in_descending_should_list_products_ordered_by_descending_name(self):
        self.header.view_category('notebooks')
        self.cate_pg.expect_category_name('Notebooks')
        self.cate_pg.sort_products_by('Name: Z to A')
        self.cate_pg.expect_url_contains('orderby=6')
        self.cate_pg.expect_sorted_product_name_in_descending()

    @pytest.mark.high
    @pytest.mark.positive
    def test_products_when_sort_by_price_from_low_to_high_should_list_products_ordered_by_low_to_high(self):
        self.header.view_category('notebooks')
        self.cate_pg.expect_category_name('Notebooks')
        self.cate_pg.sort_products_by('Price: Low to High')
        self.cate_pg.expect_url_contains('orderby=10')
        self.cate_pg.expect_sorted_price_low_to_high()

    @pytest.mark.high
    @pytest.mark.positive
    def test_products_when_sort_by_price_from_high_to_low_should_list_products_ordered_by_high_to_low(self):
        self.header.view_category('notebooks')
        self.cate_pg.expect_category_name('Notebooks')
        self.cate_pg.sort_products_by('Price: High to Low')
        self.cate_pg.expect_url_contains('orderby=11')
        self.cate_pg.expect_sorted_price_high_to_low()

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('page_size, expected_result', 
        [(3, 3), (9, 6)], 
        ids=['3 items per page', '9 items per page']
    )
    def test_products_when_select_page_size_should_list_products_less_than_or_equal_to_selected_page_size(self, page_size, expected_result):
        self.header.view_category('notebooks')
        self.cate_pg.expect_category_name('Notebooks')
        self.cate_pg.select_page_size(str(page_size))
        self.cate_pg.expect_url_contains(f'pagesize={page_size}')
        self.cate_pg.expect_total_items(expected_result)

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('page_size, expected_result', [(6, 6)], ids=['default page size: 6'])
    def test_products_when_select_default_page_size_should_list_products_less_than_or_equal_to_selected_page_size(self, page_size, expected_result):
        self.header.view_category('notebooks')
        self.cate_pg.expect_category_name('Notebooks')
        self.cate_pg.select_page_size(str(page_size))
        self.cate_pg.expect_total_items(expected_result)

    @pytest.mark.high
    @pytest.mark.positive
    @pytest.mark.parametrize('order_by, page_size, expected_result', 
        [
            (6, 3, 3),
            (11, 9, 6)
        ],
        ids = ['Order by, Name: Z to A, page_size=3', 'Order by, Price: High to Low, page_size=9']
    )
    def test_products_when_select_page_size_should_list_products_less_than_or_equal_to_selected_page_size(self, order_by, page_size, expected_result):
        self.header.view_category('notebooks')
        self.cate_pg.expect_category_name('Notebooks')
        self.cate_pg.sort_products_by_value(order_by)
        self.cate_pg.select_page_size(str(page_size))
        self.cate_pg.expect_url_contains(f'orderby={order_by}&pagesize={page_size}')
        self.cate_pg.expect_total_items(expected_result)