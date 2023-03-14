from locators.category_page import CategoryPageLocators
from page_objects.base_page import BasePage
from page_objects.components.header import HeaderComponent
from utils.helpers import sorted_list


class CategoryPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._cate_pg_locs = CategoryPageLocators
        self._header = HeaderComponent(driver)

    # Locators
    @property
    def page_heading_loc(self):
        return self._cate_pg_locs._PAGE_TITLE
    
    @property
    def sort_by_loc(self):
        return self._cate_pg_locs._SORT_BY

    @property
    def products_page_size_loc(self):
        return self._cate_pg_locs._PRODUCTS_PAGE_SIZE
    
    @property
    def product_item_loc(self):
        return self._cate_pg_locs._PRODUCT_ITEM
    
    @property
    def product_name_loc(self):
        return self._cate_pg_locs._PRODUCT_NAME
    
    @property
    def product_price_loc(self):
        return self._cate_pg_locs._PRODUCT_PRICE
       
    # Selectors
    def category_name(self):
        return self.wait_for_text(self.page_heading_loc)
    
    def sort_by(self):
        return self.find_element(self.sort_by_loc)

    def products_page_size(self):
        return self.find_element(self.products_page_size_loc)
    
    # Methods
    def expect_category_name(self, category_name):
        self.verify(self.category_name(), category_name)

    def sort_products_by(self, by: str):
        self.select_by_visible_text(self.sort_by_loc, by)

    def select_page_size(self, page_size=6):
        self.select_by_visible_text(self.products_page_size_loc, page_size)

    def sort_products_by_value(self, value):
        self.select_by_value(self.sort_by_loc, value)

    def total_items(self):
        items = self.find_elements(self.product_item_loc)
        return len(items)
    
    def list_product_name(self):
        list_product_name = self.find_texts(self.product_name_loc)
        return list_product_name
    
    def list_product_price(self):
        list_product_price = self.find_texts(self.product_price_loc)
        return list_product_price
    
    def expect_total_items(self, number):
        self.wait_for_jquery_to_load()
        self.verify(self.total_items(), number)
    
    def expect_sorted_product_name_in_ascending(self):
        self.wait_for_jquery_to_load()
        is_sorted = sorted_list(self.list_product_name())
        self.verify(is_sorted)

    def expect_sorted_product_name_in_descending(self):
        self.wait_for_jquery_to_load()
        is_reversed = sorted_list(self.list_product_name(), reverse=True)
        self.verify(is_reversed)

    def expect_sorted_price_low_to_high(self):
        self.wait_for_jquery_to_load()
        is_sorted = sorted_list(self.list_product_price())
        self.verify(is_sorted)

    def expect_sorted_price_high_to_low(self):
        self.wait_for_jquery_to_load()
        is_reversed = sorted_list(self.list_product_price(), reverse=True)
        self.verify(is_reversed)
