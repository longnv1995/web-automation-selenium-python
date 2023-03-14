from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    _PAGE_TITLE = (By.CSS_SELECTOR, 'div.page-title > h1')
    _SHIP_TO_SAME_ADDRESS_CHK = (By.CSS_SELECTOR, 'label[for="ShipToSameAddress"]')
    # STEP 1: Billing address
    _BILLING_FNAME_FIELD = (By.ID, 'BillingNewAddress_FirstName')
    _BILLING_LNAME_FIELD = (By.ID, 'BillingNewAddress_LastName')
    _BILLING_EMAIL_FIELD = (By.ID, 'BillingNewAddress_Email')
    _BILLING_COMPANY_FIELD = (By.ID, 'BillingNewAddress_Company')
    _BILLING_COUNTRY_SEL = (By.ID, 'BillingNewAddress_CountryId')
    _BILLING_STATE_SEL = (By.ID, 'BillingNewAddress_StateProvinceId')
    _BILLING_CITY_FIELD = (By.ID, 'BillingNewAddress_City')
    _BILLING_ADDRESS_ONE_FIELD = (By.ID, 'BillingNewAddress_Address1')
    _BILLING_ADDRESS_TWO_FIELD = (By.ID, 'BillingNewAddress_Address2')
    _ZIPCODE_FIELD = (By.ID, 'BillingNewAddress_ZipPostalCode')
    _PHONE_FIELD = (By.ID, 'BillingNewAddress_PhoneNumber')
    _FAX_FIELD = (By.ID, 'BillingNewAddress_FaxNumber')
    _ADDRESS_NEXT_STEP_BTN = (By.CSS_SELECTOR, 'button.new-address-next-step-button')

    # STEP 2: Shipping address is the same
    
    # STEP 3: Shipping method
    _GROUND_SHIPPING_OPT = (By.CSS_SELECTOR, 'label[for="shippingoption_0"]')
    _NEXT_DAY_SHIPPING_OPT = (By.CSS_SELECTOR, 'label[for="shippingoption_1"]')
    _2ND_DAY_SHIPPING_OPT = (By.CSS_SELECTOR, 'label[for="shippingoption_2"]')
    _SHIPPING_NEXT_STEP_BTN = (By.CSS_SELECTOR, 'button.shipping-method-next-step-button')

    
    # STEP 4: Payment method
    _CHECK_PAYMENT_OPT = (By.CSS_SELECTOR, 'label[for="paymentmethod_0"]')
    _CREDIT_CARD_PAYMENT_OPT = (By.CSS_SELECTOR, 'label[for="paymentmethod_1"]')
    _PAYMENT_NEXT_STEP_BTN = (By.CSS_SELECTOR, 'button.payment-method-next-step-button')
    
    # STEP 5: Payment information
    _PAYMENT_INFO_NEXT_STEP_BTN = (By.CSS_SELECTOR, 'button.payment-info-next-step-button')

    # Step 6: Confirm order
    _CONFIRM_ORDER_BTN = (By.CSS_SELECTOR, 'button.confirm-order-next-step-button')

    # Order completed
    _ORDER_COMPLETED_TITLE = (By.CSS_SELECTOR, 'div.title > strong')
    _ORDER_NUMBER = (By.CSS_SELECTOR, 'div.order-number > strong')
    _ORDER_DETAILS_LINK = (By.XPATH, '//a[starts-with(@href, "/orderdetails/")]')