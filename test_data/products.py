class ProductsData:
    # Desktops
    @staticmethod
    def basic_desktop():
        return {
            'name': 'Digital Storm VANQUISH 3 Custom Performance PC',
            'price': '$1,259.00',
            'sku': 'DS_VA3_PC',
            'slug': 'digital-storm-vanquish-3-custom-performance-pc',
            'min_qty': 1,
            'in_stock': True,
            'free_shipping': False,
            'type': 'desktop'
        }
    # Notebooks
    @staticmethod
    def basic_notebook():
        return {
            'name': 'HP Envy 6-1180ca 15.6-Inch Sleekbook',
            'price': '$1,460.00',
            'sku': 'HP_ESB_15',
            'slug': 'hp-envy-6-1180ca-156-inch-sleekbook',
            'min_qty': 1,
            'in_stock': True,
            'free_shipping': False,
            'type': 'notebook'
        }
    
    @staticmethod
    def notebook_min_qty_2():
        return {
            'name': 'Apple MacBook Pro 13-inch',
            'price': '$1,800.00',
            'sku': 'AP_MBP_13',
            'slug': 'apple-macbook-pro-13-inch',
            'min_qty': 2,
            'in_stock': True,
            'free_shipping': False,
            'type': 'notebook'
        }
    
    # Software
    @staticmethod
    def sold_out_software():
        return {
            'name': 'Adobe Photoshop CS4',
            'price': '$75.00',
            'sku': 'AD_CS4_PH',
            'slug': 'adobe-photoshop-cs4',
            'min_qty': 1,
            'in_stock': False,
            'free_shipping': False,
            'type': 'software'
        }
    
    def basic_hat():
        return {
            'name': 'Obey Propaganda Hat',
            'price': '$30.00',
            'sku': 'OB_HAT_PR',
            'slug': 'obey-propaganda-hat',
            'size': [34, 35, 36, 37],
            'min_qty': 1,
            'in_stock': True,
            'free_shipping': False,
            'type': 'accessory'
        }
    
    @staticmethod
    def basic_sunglass():
        return {
            'name': 'Ray Ban Aviator Sunglasses',
            'price': '$25.00',
            'sku': 'RB_AVR_SG',
            'slug': 'ray-ban-aviator-sunglasses',
            'min_qty': 1,
            'in_stock': True,
            'free_shipping': False,
            'type': 'accessory'
        }
    
    @staticmethod
    def basic_belt():
        return {
            'name': 'Reversible Horseferry Check Belt',
            'price': '$45.00',
            'sku': 'RH_CHK_BL',
            'slug': 'reversible-horseferry-check-belt',
            'min_qty': 1,
            'in_stock': True,
            'free_shipping': False,
            'type': 'accessory'
        }
    
    # Shoes
    @staticmethod
    def basic_shoe():
        return {
            'name': 'Nike SB Zoom Stefan Janoski "Medium Mint"',
            'price': '$30.00',
            'sku': 'NK_ZSJ_MM',
            'slug': 'nike-sb-zoom-stefan-janoski-medium-mint',
            'min_qty': 1,
            'in_stock': True,
            'free_shipping': False,
            'type': 'shoe'
        }
    
    @staticmethod
    def shoe_with_size_and_color():
        return {
            'name': 'adidas Consortium Campus 80s Running Shoes',
            'price': '$27.56',
            'sku': 'AD_C80_RS',
            'slug': 'adidas-consortium-campus-80s-running-shoes',
            'min_qty': 1,
            'in_stock': True,
            'free_shipping': False,
            'type': 'shoe'
        }
    
    # Books 
    @staticmethod
    def new_price_book():
        return {
            'name': 'First Prize Pies',
            'short_desc': 'First Prize Pies',
            'old_price': '$67.00',
            'price': '$51.00',
            'sku': 'FIRST_PRP',
            'free_shipping': False,
            'slug': 'first-prize-pies',
            'min_qty': 1,
            'in_stock': True,
            'type': 'book'
        }
    
    @staticmethod
    def new_price_and_free_shipping_book():
        return {
            'name': 'Fahrenheit 451 by Ray Bradbury',
            'old_price': '$30.00',
            'price': '$27.00',
            'sku': 'FR_451_RB',
            'slug': 'fahrenheit-451-by-ray-bradbury',
            'free_shipping': True,
            'min_qty': 1,
            'in_stock': True,
            'type': 'book'
        }