class OrdersData:
    # Desktops
    @staticmethod
    def required_billing_fields():
        return {
            'first_name': 'long',
            'last_name': 'nguyen van',
            'email': 'long.nguyenvan@gmail.com',
            'country': 'Viet Nam',
            'city': 'Ha Noi',
            'address_one': 'Thuong Tin, Ha Noi',
            'zipcode': '10000',
            'phone': '0945444421'
        }
    
    @staticmethod
    def full_billing_fields():
        return {
            'first_name': 'long',
            'last_name': 'nguyen van',
            'email': 'long.nguyenvan@gmail.com',
            'company': 'Optimizely',
            'country': 'Viet Nam',
            'state': 'Other',
            'city': 'Ha Noi',
            'address_one': 'Thuong Tin, Ha Noi',
            'address_two': 'Cau Giay, Ha Noi',
            'zipcode': '10000',
            'phone': '0945444429',
            'fax': '232324'
        }
    
    @staticmethod
    def credit_card_data():
        return {
            'card_name': 'Nguyen Van Long',
            'card_number': '4242424242424242',
            'exp_date': '01',
            'exp_year': '2023',
            'code': '123'
        }
    
    @staticmethod
    def ground_shipping_method():
        return {
            'method': 'Ground ($0.00)',
            'description': 'Shipping by land transport'
        }

    @staticmethod
    def next_day_shipping_method():
        return {
            'method': 'Next Day Air ($0.00)',
            'description': 'The one day air shipping'
        }

    @staticmethod
    def second_day_shipping_method():
        return {
            'method': '2nd Day Air ($0.00)',
            'description': 'The two day air shipping'
        }
    
    @staticmethod
    def cheque_payment():
        return {
            'method': 'Check / Money Order',
            'description': 'Pay by cheque or money order'
        }