import pytest
from page_objects.components.footer import FooterComponent

from page_objects.components.header import HeaderComponent
from page_objects.components.main_area import MainComponent
from page_objects.components.sidebar import SidebarComponent
from page_objects.login_page import LoginPage
from utils.helpers import verify_links


class TestImageLinks:
    @pytest.fixture(scope='function', autouse=True)
    def before_test(self, driver):
        self.header = HeaderComponent(driver)
        self.footer = FooterComponent(driver)
        self.main_area = MainComponent(driver)
        self.sidebar = SidebarComponent(driver)
        self.login_pg = LoginPage(driver)

    def test_all_images_in_header_should_not_broken(self):
        _image_links = self.header.find_images_in_header()
        result = verify_links(_image_links)
        assert result['total_broken_links'] == 0

    def test_all_images_in_menu_should_not_broken(self):
        _image_links = self.header.find_images_in_menu()
        result = verify_links(_image_links)
        assert result['total_broken_links'] == 0

    @pytest.mark.skip('Takes time to run. Skip for now')
    def test_all_images_in_footer_should_not_broken(self):
        _image_links = self.footer.find_images_in_footer()
        result = verify_links(_image_links)
        assert result['total_broken_links'] == 0

    @pytest.mark.skip('Takes time to run. Skip for now')
    def test_all_images_in_sidebar_should_not_broken(self):
        self.header.navigate_to('/desktops')
        _image_links = self.sidebar.find_images_in_sidebar()
        result = verify_links(_image_links)
        assert result['total_broken_links'] == 0

    @pytest.mark.skip('Takes time to run. Skip for now')
    def test_all_images_in_main_page_should_not_broken(self):
        _image_links = self.main_area.find_images_in_main_area()
        result = verify_links(_image_links)
        assert result['total_broken_links'] == 0
