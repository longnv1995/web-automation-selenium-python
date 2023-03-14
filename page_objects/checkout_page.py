from locators.checkout_page import CheckoutPageLocators
from page_objects.base_page import BasePage
from page_objects.components.header import HeaderComponent


class CheckoutPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._checkout_pg = CheckoutPageLocators
        self._header = HeaderComponent(driver)

    # Locators
    # step 1 & 2
    @property
    def page_heading_loc(self):
        return self._checkout_pg._PAGE_TITLE
    
    @property
    def ship_to_same_address_loc(self):
        return self._checkout_pg._SHIP_TO_SAME_ADDRESS_CHK
    
    @property
    def billing_fname_loc(self):
        return self._checkout_pg._BILLING_FNAME_FIELD
    
    @property
    def billing_lname_loc(self):
        return self._checkout_pg._BILLING_LNAME_FIELD
    
    @property
    def billing_email_loc(self):
        return self._checkout_pg._BILLING_EMAIL_FIELD
    
    @property
    def billing_company_loc(self):
        return self._checkout_pg._BILLING_COMPANY_FIELD
    
    @property
    def billing_country_loc(self):
        return self._checkout_pg._BILLING_COUNTRY_SEL
    
    @property
    def billing_state_loc(self):
        return self._checkout_pg._BILLING_STATE_SEL
    
    @property
    def billing_city_loc(self):
        return self._checkout_pg._BILLING_CITY_FIELD
    
    @property
    def billing_address_one_loc(self):
        return self._checkout_pg._BILLING_ADDRESS_ONE_FIELD
    
    @property
    def billing_address_two_loc(self):
        return self._checkout_pg._BILLING_ADDRESS_TWO_FIELD
    
    @property
    def zipcode_loc(self):
        return self._checkout_pg._ZIPCODE_FIELD
    
    @property
    def phone_loc(self):
        return self._checkout_pg._PHONE_FIELD
    
    @property
    def fax_loc(self):
        return self._checkout_pg._FAX_FIELD
    
    @property
    def address_next_step_loc(self):
        return self._checkout_pg._ADDRESS_NEXT_STEP_BTN
    
    # step 3
    @property
    def groud_shipping_loc(self):
        return self._checkout_pg._GROUND_SHIPPING_OPT
    
    @property
    def next_day_shipping_loc(self):
        return self._checkout_pg._NEXT_DAY_SHIPPING_OPT
    
    @property
    def second_day_shipping(self):
        return self._checkout_pg._2ND_DAY_SHIPPING_OPT
    
    @property
    def fax_loc(self):
        return self._checkout_pg._FAX_FIELD
    
    @property
    def shipping_method_next_step_loc(self):
        return self._checkout_pg._SHIPPING_NEXT_STEP_BTN

    # step 4
    @property
    def check_payment_loc(self):
        return self._checkout_pg._CHECK_PAYMENT_OPT
    
    @property
    def credit_card_payment_loc(self):
        return self._checkout_pg._CREDIT_CARD_PAYMENT_OPT
    
    @property
    def payment_next_step_loc(self):
        return self._checkout_pg._PAYMENT_NEXT_STEP_BTN
    
    # step 5
    @property
    def payment_info_next_step_loc(self):
        return self._checkout_pg._PAYMENT_INFO_NEXT_STEP_BTN

    # step 6
    @property
    def confirm_order_loc(self):
        return self._checkout_pg._CONFIRM_ORDER_BTN
    
    @property
    def order_completed_title_loc(self):
        return self._checkout_pg._ORDER_COMPLETED_TITLE
    
    @property
    def order_number_loc(self):
        return self._checkout_pg._ORDER_NUMBER
    
    @property
    def order_details_loc(self):
        return self._checkout_pg._ORDER_DETAILS_LINK
    
    # Selectors
    def order_completed_title(self):
        return self.wait_for_text(self.order_completed_title_loc)
    
    # Action
    def click_address_next_step_btn(self): # step1
        self.wait_for_click(self.address_next_step_loc)

    def click_shipping_method_next_step_btn(self): # step3
        self.wait_for_click(self.shipping_method_next_step_loc)

    def click_payment_next_step_btn(self): # step4
        self.wait_for_click(self.payment_next_step_loc)

    def click_payment_info_next_step_btn(self): # step5
        self.wait_for_click(self.payment_info_next_step_loc)

    def click_confirm_btn(self): # step6 (last step)
        self.wait_for_click(self.confirm_order_loc)

    # Methods
    def fill_in_billing_form(self, data):
        _keys = list(data.keys())

        if 'first_name' in _keys:
            self.enter_text(self.billing_fname_loc, data['first_name'])

        if 'last_name' in _keys:
            self.enter_text(self.billing_lname_loc, data['last_name'])
        
        if 'email' in _keys:
            self.enter_text(self.billing_email_loc, data['email'])
        
        if 'company' in _keys:
            self.enter_text(self.billing_company_loc, data['company'])
        
        if 'country' in _keys:
            self.select_by_visible_text(self.billing_country_loc, data['country'])

        self.wait_for_jquery_to_load()

        if 'state' in _keys:
            self.select_by_visible_text(self.billing_state_loc, data['state'])

        if 'city' in _keys:
            self.enter_text(self.billing_city_loc, data['city'])
        
        if 'address_one' in _keys:
            self.enter_text(self.billing_address_one_loc, data['address_one'])

        if 'address_two' in _keys:
            self.enter_text(self.billing_address_two_loc, data['address_two'])

        if 'zipcode' in _keys:
            self.enter_text(self.zipcode_loc, data['zipcode'])

        if 'phone' in _keys:
            self.enter_text(self.phone_loc, data['phone'])

        if 'fax' in _keys:
            self.enter_text(self.fax_loc, data['fax'])

    def fill_in_billing_form_and_continue(self, data):
        self.fill_in_billing_form(data)
        self.click_address_next_step_btn()

    def select_shipping_method_and_continue(self):
        # select default shipping method for now
        self.wait_for_jquery_to_load()
        self.click_shipping_method_next_step_btn()

    def select_payment_method_and_continue(self):
        self.wait_for_jquery_to_load()
        # select default payment method for now
        self.click_payment_next_step_btn()

    def check_payment_info_and_continue(self):
        self.wait_for_jquery_to_load()
        self.click_payment_info_next_step_btn()

    def confirm_order(self):
        self.wait_for_jquery_to_load()
        self.click_confirm_btn()
        self.wait_for_jquery_to_load()

    def expect_order_completed_title(self, text):
        self.verify(self.order_completed_title(), text)

    def view_order_details(self):
        self.wait_for_click(self.order_details_loc)