import time
from locators.cart_page import CartPageLocators
from page_objects.base_page import BasePage
from page_objects.components.header import HeaderComponent
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._cart_pg = CartPageLocators
        self._header = HeaderComponent(driver)

    # Locators
    @property
    def page_heading_loc(self):
        return self._cart_pg._PAGE_TITLE
    
    @property
    def cart_item_loc(self):
        return self._cart_pg._CART_ITEM
    
    @property
    def sku_heading_loc(self):
        return self._cart_pg._SKU_HEADING
    
    @property
    def image_heading_loc(self):
        return self._cart_pg._IMAGE_HEADING
    
    @property
    def product_heading_loc(self):
        return self._cart_pg._PRODUCT_HEADING
    
    @property
    def unit_price_heading_loc(self):
        return self._cart_pg._UNIT_PRICE_HEADING
    
    @property
    def qty_heading_loc(self):
        return self._cart_pg._QTY_HEADING
    
    @property
    def qty_item_loc(self):
        return self._cart_pg._QTY_ITEM_FIELD
    
    @property
    def update_qty_error(self):
        return self._cart_pg._UPDATE_QTY_ERROR
    
    @property
    def subtotal_heading_loc(self):
        return self._cart_pg._SUBTOTAL_HEADING
    
    @property
    def remove_product_heading_loc(self):
        return self._cart_pg._REMOVE_FROM_CART_HEADING
    
    @property
    def discount_loc(self):
        return self._cart_pg._DISCOUNT_FIELD
    
    @property
    def discount_msg_loc(self):
        return self._cart_pg._DISCOUNT_MSG
    
    @property
    def gift_card_loc(self):
        return self._cart_pg._GIFT_CARD_FIELD
    
    @property
    def gift_card_msg_loc(self):
        return self._cart_pg._GIFT_CARD_MSG
    
    @property
    def apply_discount_loc(self):
        return self._cart_pg._APPLY_COUPLE_BTN
    
    @property
    def apply_gift_card_loc(self):
        return self._cart_pg._APPLY_GIFT_CARD_BTN
    
    @property
    def terms_loc(self):
        return self._cart_pg._TERMS_CHK
    
    @property
    def checkout_loc(self):
        return self._cart_pg._CHECKOUT_BTN
    
    @property
    def empty_cart_loc(self):
        return self._cart_pg._EMPTY_CART
    
    @property
    def remove_loc(self):
        return self._cart_pg._REMOVE_BTN
    
    @property
    def update_cart_loc(self):
        return self._cart_pg._UPDATE_CART_BTN
    
    # Selectors
    def page_heading(self):
        return self.wait_for_text(self.page_heading_loc)
    
    def discount_msg(self):
        return self.wait_for_text(self.discount_msg_loc)
    
    def gift_card_msg(self):
        return self.wait_for_text(self.gift_card_msg_loc)
    
    def cart_items(self):
        return self.wait_for_elements(self.cart_item_loc)
    
    def terms_of_service(self):
        return self.wait_for_element(self.terms_loc)
    
    def checkout_btn(self):
        return self.wait_for_element(self.checkout_loc)
    
    def empty_cart_msg(self):
        return self.wait_for_text(self.empty_cart_loc)
    
    # Actions
    def click_apply_discount_btn(self):
        self.click(self.apply_discount_loc)

    def click_apply_gift_card_btn(self):
        self.click(self.apply_gift_card_loc)

    def check_agree_terms(self):
        self.click(self.terms_loc)

    def click_checkout_btn(self):
        self.scroll_into_view_if_needed(self.find_element(self.checkout_loc))
        self.click(self.checkout_loc)

    def click_update_cart_btn(self):
        self.click(self.update_cart_loc)
        self.wait_for_js_and_jquery_to_load()

    # Methods
    def expect_updated_cart_successfully_and_showed_msg(self, msg, qty=1):
        self.verify(self.add_to_cart_alert_msg(), msg)
        self.verify(self._header.cart_qty(), f'({qty})')

    def expect_updated_cart_failed_and_showed_error_msg(self, msg):
        self.verify(self.add_to_cart_alert_msg(), msg)

    def expect_page_heading(self, text):
        self.verify(self.page_heading(), text)

    def expect_empty_cart_msg(self, text):
        self.verify(self.empty_cart_msg(), text)

    def expect_cart_items(self, items):
        self.verify(len(self.cart_items()), items)

    def expect_discount_error_msg(self, msg):
        self.verify(self.discount_msg(), msg)

    def expect_gift_card_error_msg(self, msg):
        self.verify(self.gift_card_msg(), msg)

    def apply_discount(self, value):
        self.enter_text(self.discount_loc, value)
        self.click_apply_discount_btn()

    def apply_gift_card(self, value):
        self.enter_text(self.gift_card_loc, value)
        self.click_apply_gift_card_btn()

    def remove_products(self):
        remove_btn_list = self.find_elements(self.remove_loc)
        for remove_btn in remove_btn_list:
            self.wait_for_click(self.remove_loc)
            

    """
    Not find a good way to handle these situations yet. Come back later
    """
    def remove_product(self, product):
        for elem in self.cart_items():
            if product['name'] in elem.text:
                remove_btn_elem = elem.find_element(*self.remove_loc)
                remove_btn_elem.click()
                break
    
    def update_qty_and_wait_for_successfully(self, product, qty):
        """
        pass positive number for qty when using this func
        """
        for elem in self.cart_items():
            if product['name'] in elem.text:
                qty_elem = elem.find_element(*self.qty_item_loc)
                qty_elem.clear()
                qty_elem.send_keys(qty)
                self.click_update_cart_btn()
                try:
                    time.sleep(1)
                    self.verify(elem.find_element(*self.qty_item_loc).get_attribute('value'), str(qty))
                except StaleElementReferenceException:
                    time.sleep(1)
                    self.verify(elem.find_element(*self.qty_item_loc).get_attribute('value'), str(qty))

    def update_qty_and_expect_eror(self, product, qty, msg):
        """
        pass negative number for qty when using this func
        """
        for elem in self.cart_items():
            if product['name'] in elem.text:
                qty_elem = elem.find_element(*self.qty_item_loc)
                orginal_qty = qty_elem.get_attribute('value')
                qty_elem.clear()
                qty_elem.send_keys(qty)
                self.click_update_cart_btn()
                list_error_msgs = self.find_texts(self.update_qty_error)
                self.assert_in(msg, list_error_msgs)
                # self.verify(elem.find_element(*self.qty_item_loc).get_attribute('value'), orginal_qty)