from locators.components.main_area import MainAreaLocators
from page_objects.base_page import BasePage


class MainComponent(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._main_locs = MainAreaLocators

    # Locators
    @property
    def link_loc(self):
        return self._main_locs._LINK
    
    @property
    def image_loc(self):
        return self._main_locs._IMAGE
    
    @property
    def main_area_loc(self):
        return self._main_locs._MAIN_AREA
    
    # Methods
    def find_links_in_main_area(self) -> list:
        return self.find_links_from(self.link_loc, self.main_area_loc)
    
    def find_images_in_main_area(self) -> list:
        return self.find_images_from(self.image_loc, self.main_area_loc)