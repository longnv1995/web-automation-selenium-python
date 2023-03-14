from locators.components.sidebar import SidebarLocators
from page_objects.base_page import BasePage


class SidebarComponent(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._sidebar_locs = SidebarLocators

    # Locators
    @property
    def link_loc(self):
        return self._sidebar_locs._LINK
    
    @property
    def image_loc(self):
        return self._sidebar_locs._IMAGE
    
    @property
    def sidebar_loc(self):
        return self._sidebar_locs._SIDEBAR
    
    # Methods
    def find_links_in_sidebar(self) -> list:
        return self.find_links_from(self.image_loc, self.sidebar_loc)   
    
    def find_images_in_sidebar(self) -> list:
        return self.find_images_from(self.image_loc, self.sidebar_loc)   