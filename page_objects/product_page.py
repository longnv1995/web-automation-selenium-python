from locators.product_page import ProductPageLocators
from page_objects.base_page import BasePage
from page_objects.components.header import HeaderComponent
from utils.custom_enums import ProductType
from utils.helpers import get_enum_values


class ProductPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._product_pg = ProductPageLocators
        self._header = HeaderComponent(driver)

    # Locators
    @property
    def name_loc(self):
        return self._product_pg._NAME
    
    @property
    def short_desc_loc(self):
        return self._product_pg._SHORT_DESC
    
    @property
    def sku_loc(self):
        return self._product_pg._SKU
    
    @property
    def free_shipping_loc(self):
        return self._product_pg._FREE_SHIPPING

    @property
    def old_price_loc(self):
        return self._product_pg._OLD_PRICE

    @property
    def price_loc(self):
        return self._product_pg._PRICE
    
    @property
    def qty_loc(self):
        return self._product_pg._QTY_FIELD
    
    @property
    def add_to_cart_loc(self):
        return self._product_pg._ADD_TO_CART_BTN
    
    @property
    def alert_msg_loc(self):
        return self._product_pg._ALERT_MSG
    
    @property
    def link_to_cart(self):
        return self._product_pg._LINK_TO_CART
    
    @property
    def size_loc(self):
        return self._product_pg._SIZE

    # Selectors
    def product_name(self):
        return self.wait_for_text(self.name_loc)
    
    def product_sku(self):
        return self.find_text(self.sku_loc)
    
    def product_free_shipping(self):
        return self.find_text(self.free_shipping_loc)
    
    def old_product_pricing(self):
        return self.find_text(self.old_price_loc)
        
    def product_pricing(self):
        return self.find_text(self.price_loc)
    
    def qty(self):
        return self.find_attribute(self.qty_loc, 'value')
    
    def add_to_cart_alert_msg(self):
        return self.wait_for_text(self.alert_msg_loc)
    
    def size_opts(self):
        return self.find_element(self.size_loc)
    
    # Actions
    def click_add_to_cart_btn(self):
        self.wait_for_click(self.add_to_cart_loc)

    def view_cart(self):
        pass

    def click_link_to_view_cart(self):
        self.click(self.link_to_cart)

    def add_qty(self, number=1):
        self.enter_text(self.qty_loc, number)

    def select_size(self, text):
        return self.select_by_visible_text(self.size_loc, text)
    
    def select_color(self, text):
        return self.select_by_visible_text(self.size_loc, text)

    # Methods
    def expect_added_to_cart_successfully(self, msg):
        self.verify(self.add_to_cart_alert_msg(), msg)

    def expect_cart_qty(self, qty=1):
        self.verify(self._header.cart_qty(), f'({qty})')

    def expect_add_to_cart_failed(self, msg):
        self.verify(self.add_to_cart_alert_msg(), msg)

    def expect_product_name(self, product):
        self.verify(self.product_name(), product['name'])

    def __verify_basic_product_info(self, product):
        _product_keys = list(product.keys())
        self.verify(self.product_name(), product['name'])
        self.verify(self.product_sku(), product['sku'])
        
        if 'free_shipping' in _product_keys and product['free_shipping']:
            self.verify(self.product_free_shipping(), 'Free shipping')

        if 'old_price' in _product_keys:
            self.verify(self.old_product_pricing(), product['old_price'])

    def verify_product_details(self, product):
        _product_types = get_enum_values(ProductType)

        if product['type'] not in _product_types:
            raise KeyError(f'Not a valid product type.')
        
        self.__verify_basic_product_info(product)

        if product['type'] == ProductType.BOOK:
           pass

        if product['type'] == ProductType.DESKTOP:
            pass

        if product['type'] == ProductType.SOFTWARE:
            pass

        if product['type'] == ProductType.NOTEBOOK:
            pass

        if product['type'] == ProductType.ACCESSORY:
            pass

        if product['type'] == ProductType.SHOE:
            pass

        
    