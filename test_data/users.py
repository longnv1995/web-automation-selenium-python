from faker import Faker


fake_data = Faker()

class UsersData:
    @staticmethod
    def valid_user():
        return {'email': 'autotest_lonv@gmail.com', 'password': 123456}
    
    @staticmethod
    def invalid_email_format():
        return {'email': 'random', 'password': 123456}
    
    @staticmethod
    def non_existing_user():
        return {'email': 'random@gmail.com', 'password': 123456}
    
    @staticmethod
    def invalid_password():
        return {'email': 'test@gmail.com', 'password': 'abcdef'}
    
class RegisterUsersData:
    @staticmethod
    def required_fields_are_fullfill():
        return {
            'first_name': 'long', 
            'last_name': 'nguyen van', 
            'email': fake_data.email(), 
            'password': '123456',
            'confirm_pass': '123456'
        }
    
    @staticmethod
    def all_fields_are_fullfill():
        return {
            'gender': 'male',
            'first_name': 'long', 
            'last_name': 'nguyen van', 
            'dob_day': '12',
            'dob_month': '12',
            'dob_year': '1995',
            'email': fake_data.email(), 
            'company': 'Optimizely',
            'password': '123456',
            'confirm_pass': '123456'
        }
    
    @staticmethod
    def no_match_password():
        return {
            'first_name': 'long', 
            'last_name': 'nguyen van', 
            'email': fake_data.email(), 
            'password': '123@56',
            'confirm_pass': '123456'
        }
    
    @staticmethod
    def invalid_email_format():
        return {
            'first_name': 'long', 
            'last_name': 'nguyen van', 
            'email': 'randomstr', 
            'password': '123456',
            'confirm_pass': '123456'
        }
    
    @staticmethod
    def invalid_min_lenth_password():
        return {
            'first_name': 'long', 
            'last_name': 'nguyen van', 
            'email': 'randomstr@gmail.com', 
            'password': '123',
            'confirm_pass': '123'
        }