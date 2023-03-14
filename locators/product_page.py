from selenium.webdriver.common.by import By


class ProductPageLocators:
    _NAME = (By.CSS_SELECTOR, 'div.product-name > h1')
    _SHORT_DESC = (By.CSS_SELECTOR, 'div.short-description')
    _SKU = (By.CSS_SELECTOR, 'div.sku > span.value')
    _OLD_PRICE = (By.CSS_SELECTOR, 'div.old-product-price > span:nth-child(2)')
    _PRICE = (By.CSS_SELECTOR, 'div.product-price > span') #price
    _SIZE = (By.XPATH, '//select[starts-with(@id, "product_attribute_")]')
    _FREE_SHIPPING = (By.CSS_SELECTOR, 'div.free-shipping')
    _QTY_FIELD = (By.XPATH, '//input[starts-with(@id, "product_enteredQuantity_")]')
    _ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.add-to-cart-button')
    _ADD_TO_WISHLIST_BTN = (By.CSS_SELECTOR, 'button.add-to-wishlist-button')
    _ADD_TO_COMPARE_LIST_BTN = (By.CSS_SELECTOR, 'button.add-to-compare-list-button')
    _NOTIFICATION_BAR = (By.ID, 'bar-notification')
    _ALERT_MSG = (By.CSS_SELECTOR, 'div.bar-notification p.content')
    _LINK_TO_CART = (By.CSS_SELECTOR, 'div.bar-notification a')