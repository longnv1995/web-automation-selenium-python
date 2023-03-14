from selenium.webdriver.common.by import By


class CategoryPageLocators:
    _PAGE_TITLE = (By.CSS_SELECTOR, 'div.page-title > h1')
    _SORT_BY = (By.ID, 'products-orderby')
    _PRODUCTS_PAGE_SIZE = (By.ID, 'products-pagesize')
    _PRODUCT_GRID = (By.CSS_SELECTOR, 'div.product-grid')
    _PRODUCT_ITEM = (By.CSS_SELECTOR, 'div.product-item')
    _PRODUCT_NAME = (By.CSS_SELECTOR, 'h2.product-title > a')
    _PRODUCT_PRICE = (By.CSS_SELECTOR, 'span[class="price actual-price"]')
