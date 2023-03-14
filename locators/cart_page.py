from selenium.webdriver.common.by import By


class CartPageLocators:
    _PAGE_TITLE = (By.CSS_SELECTOR, 'div.page-title > h1')
    _CART_ITEM = (By.CSS_SELECTOR, 'table.cart > tbody > tr')
    _SKU_HEADING = (By.CSS_SELECTOR, 'table.cart th.sku')
    _IMAGE_HEADING = (By.CSS_SELECTOR, 'table.cart th.product-picture')
    _PRODUCT_HEADING = (By.CSS_SELECTOR, 'table.cart th.product')
    _UNIT_PRICE_HEADING = (By.CSS_SELECTOR, 'table.cart th.unit-price')
    _QTY_HEADING = (By.CSS_SELECTOR, 'table.cart th.quantity')
    _QTY_ITEM_FIELD = (By.CSS_SELECTOR, 'input.qty-input')
    _UPDATE_QTY_ERROR = (By.CSS_SELECTOR, 'div.message-error > ul > li')
    _SUBTOTAL_HEADING = (By.CSS_SELECTOR, 'table.cart th.subtotal')
    _REMOVE_FROM_CART_HEADING = (By.CSS_SELECTOR, 'table.cart th.remove-from-cart')
    _REMOVE_BTN = (By.CSS_SELECTOR, 'button.remove-btn')
    _EMPTY_CART = (By.CSS_SELECTOR, 'div.order-summary-content > div.no-data')

    _UPDATE_CART_BTN = (By.ID, 'updatecart')
    _CONTINUE_SHOPPING_BTN = (By.NAME, 'continueshopping')
    _ESTIMATE_SHIPPING_FEE_BTN = (By.ID, 'open-estimate-shipping-popup')
    
    _GIFT_WRAPPING = (By.CSS_SELECTOR, 'select#checkout_attribute_1')
    _SELECTED_GIFT_WRAPPING = (By.CSS_SELECTOR, 'div.selected-checkout-attributes')

    _DISCOUNT_FIELD = (By.ID, 'discountcouponcode')
    _DISCOUNT_MSG = (By.CSS_SELECTOR, 'div.coupon-box > div.message-failure')
    _APPLY_COUPLE_BTN = (By.ID, 'applydiscountcouponcode')
    _GIFT_CARD_FIELD = (By.ID, 'giftcardcouponcode')
    _GIFT_CARD_MSG = (By.CSS_SELECTOR, 'div.giftcard-box > div.message-failure')
    _APPLY_GIFT_CARD_BTN = (By.ID, 'applygiftcardcouponcode')

    _SUBTOTAL_LABEL = (By.CSS_SELECTOR, 'tr.order-subtotal label')
    _SUBTOTAL = (By.CSS_SELECTOR, 'tr.order-subtotal value-summary')
    _SHIPPING_LABEL = (By.CSS_SELECTOR, 'tr.shipping-cost label')
    _SHIPPING = (By.CSS_SELECTOR, 'tr.shipping-cost value-summary')
    _TAX_LABEL = (By.CSS_SELECTOR, 'tr.tax-value label')
    _TAX = (By.CSS_SELECTOR, 'tr.tax-value value-summary')
    _TOTAL_LABEL = (By.CSS_SELECTOR, 'tr.order-total label')
    _TOTAL = (By.CSS_SELECTOR, 'tr.order-total value-summary')
    _TERMS_CHK = (By.ID, 'termsofservice')
    _READ_TERMS = (By.ID, 'read-terms')
    _CHECKOUT_BTN = (By.ID, 'checkout')
    
    # Shipping fee dialog
    _ESTIMATE_SHIPPING_FEE_POPUP = (By.ID, 'estimate-shipping-popup')
    _SHIP_TO = (By.CSS_SELECTOR, 'div.ship-to-title > strong')
    _COUNTRY = (By.ID, 'CountryId')
    _STATE = (By.ID, 'StateProvinceId')
    _ZIP_CODE = (By.ID, 'ZipPostalCode')
    _SHIPPING_METHOD = (By.CSS_SELECTOR, 'div.choose-shipping-title > strong')
    _APPLY_SHIPPING_BTN = (By.CSS_SELECTOR, 'button[class="button-2 apply-shipping-button"]')
    _CLOSE_BTN = (By.CSS_SELECTOR, 'button[title="Close (Esc)"]')