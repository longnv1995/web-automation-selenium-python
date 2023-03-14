from locators.components.footer import FooterLocators
from page_objects.base_page import BasePage


class FooterComponent(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._footer_locs = FooterLocators

    # Locators
    @property
    def link_loc(self):
        return self._footer_locs._LINK
    
    @property
    def image_loc(self):
        return self._footer_locs._IMAGE
    
    @property
    def footer_loc(self):
        return self._footer_locs._FOOTER
    
    # Selectors
    def find_links_in_footer(self) -> list:
        return self.find_links_from(self.link_loc, self.footer_loc)
    
    def find_images_in_footer(self) -> list:
        return self.find_images_from(self.image_loc, self.footer_loc)