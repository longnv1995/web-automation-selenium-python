from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from pathlib import Path
from datetime import datetime



TIMEOUT_IN_SECS = 10
BASE_URL = 'https://demo.nopcommerce.com/'


class BasePage(object):
    def __init__(self, driver)->None:
        self._driver = driver
        self._wait = self.__init_wait()
        self._AC = ActionChains(self._driver)
    
    def __init_wait(self):
        return WebDriverWait(self._driver, 
                             timeout=TIMEOUT_IN_SECS, 
                             poll_frequency=0.5, 
                             ignored_exceptions=[NoSuchElementException, 
                                                 ElementNotVisibleException, 
                                                 ElementNotInteractableException, 
                                                 StaleElementReferenceException])

    def __wait_for_visible_element(self, locator):
        """
        Wait for element is present on the DOM of a page and visible
        Return: first element found within a givin context if found mutilple elements on a page
        """
        _element = None
        try:
            _element = self._wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Not found element with locator: {locator} within givin time, {TIMEOUT_IN_SECS}')
        
        return _element

    def __wait_for_visible_elements(self, locator):
        """
        Wait for elements are present on the DOM of a page and visible
        Return: all matched elements on a page
        """
        _elements = []
        try:
            _elements = self._wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            print(f'Not found element with locator: {locator} within givin time, {TIMEOUT_IN_SECS}')

        return _elements

    def __wait_for_invisible_element(self, locator):
        """
        Wait for element is not present on the DOM of a page or invisible
        """
        _result = False
        try:
            _result = self._wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            print(f'Element is still displayed: {locator} after givin time, {TIMEOUT_IN_SECS}')
        
        return _result
    
    def __element_to_be_clickable(self, locator):
        """
        Wait for element is visible and enabled
        """
        _element = None
        try:
            _element = self._wait.until(EC.element_to_be_clickable(locator))
        except ElementNotVisibleException:
            print(f'Not found element with locator: {locator} within givin time, {TIMEOUT_IN_SECS}')
        except ElementNotInteractableException:
            print(f'Cannot click on: {locator}')

        return _element
    
    def __find_element(self, locator):
        _element = None
        try:
            _element = self._driver.find_element(*locator)
        except NoSuchElementException:
            print(f'Not found element with locator with locator: {locator}')
        except ElementNotVisibleException:
            print(f'Element is not visible to interact with, locator: {locator}')
        
        return _element
    
    def __find_elements(self, locator):
        _elements = []
        try:
            _elements = self._driver.find_elements(*locator)
        except NoSuchElementException:
            print(f'Not found element with locator with locator: {locator}')
        except ElementNotVisibleException:
            print(f'Element is not visible to interact with, locator: {locator}')
        
        return _elements
    
    def find_element(self, locator):
        return self.__find_element(locator)
    
    def find_elements(self, locator):
        return self.__find_elements(locator)
    
    def find_element_from(self, lower_loc, upper_loc):
        upper_loc = self.wait_for_element(upper_loc)
        element = upper_loc.find_element(*lower_loc)
        return element
    
    def find_elements_from(self, lower_loc, upper_loc):
        upper_loc = self.wait_for_element(upper_loc)
        elements = upper_loc.find_elements(*lower_loc)
        return elements
    
    def find_text(self, locator):
        return self.__find_element(locator).text
    
    def find_texts(self, locator):
        elements = self.__find_elements(locator)
        return [element.text for element in elements]
    
    def find_attribute(self, locator, attribute):
        return self.__find_element(locator).get_attribute(attribute)
    
    def __find_source_from(self, lower_loc, upper_loc, attribute):
        _source = []
        elements = self.find_elements_from(lower_loc, upper_loc)
        for e in elements:
            _source.append(e.get_attribute(attribute))

        return _source
    
    def find_links_from(self, lower_loc, upper_loc):
        return self.__find_source_from(lower_loc, upper_loc, 'href')
    
    def find_images_from(self, lower_loc, upper_loc):
        return self.__find_source_from(lower_loc, upper_loc, 'src')
    
    def wait_for_element(self, locator):
        return self.__wait_for_visible_element(locator)
    
    def click(self, locator):
        element = self._driver.find_element(*locator)
        self._driver.execute_script('arguments[0].scrollIntoViewIfNeeded(true);', element)
        element.click()

    def wait_for_elements(self, locator):
        return self.__wait_for_visible_elements(locator)

    def wait_for_text(self, locator):
        """
        Get text of visible element
        """
        return self.__wait_for_visible_element(locator).text
    
    def wait_for_texts(self, locator):
        """
        Get text of all visible elements
        """
        elements = self.wait_for_elements(locator)
        return [element.text for element in elements]
    
    def wait_for_attribute(self, locator, attribute):
        """
        Get attribute of visible element
        """
        return self.__wait_for_visible_element(locator).get_attribute(attribute)

    def wait_for_click(self, locator):
        """
        Wait for element visible and clickable
        """
        self.__element_to_be_clickable(locator).click()

    def wait_for_enabled(self, locator):
        is_enabled = self.__element_to_be_clickable(locator)
        return bool(is_enabled)
    
    def wait_for_disabled(self, locator):
        return bool(self.wait_for_enabled())
    
    def wait_for_visible(self, locator) -> bool:
        is_visible = self.__wait_for_visible_element(locator)
        return bool(is_visible)
        
    def wait_for_hidden(self, locator) -> bool:
        is_hidden = self.__wait_for_invisible_element(locator)
        return bool(is_hidden)
    
    def wait_for_disappeared(self, locator) -> bool:
        is_disappeared = self.__wait_for_invisible_element(locator)
        return bool(is_disappeared)

    def enter_text(self, locator, text):
        element = self.__find_element(locator)
        element.clear()
        if text is not None:
            element.send_keys(text)

    def select_by_index(self, locator, index):
        select = Select(self.find_element(locator))
        _result = select.select_by_index(int(index))
        return _result

    def select_by_visible_text(self, locator, value):
        select = Select(self.find_element(locator))
        _result = select.select_by_visible_text(str(value))
        return _result
    
    def select_by_value(self, locator, value):
        select = Select(self.find_element(locator))
        _result = select.select_by_value(str(value))
        return _result
    
    # ACTIONS
    def right_click(self, locator):
        clickable_elem = self.__find_element(locator)
        self._AC.context_click(clickable_elem).perform()

    def double_click(self, locator):
        clickable_elem = self.__find_element(locator)
        self._AC.double_click(clickable_elem).perform()

    def drag_and_drop(self, source, target):
        draggable_elem = self.__find_element(source)
        droppable_elem = self.__find_element(target)
        self._AC.drag_and_drop(draggable_elem, droppable_elem).perform()
    
    def hover(self, element):
        return self._AC.move_to_element(element).perform()

    # SCROLL PAGE
    def scroll_up(self, num_pixels):
        self._driver.execute_script(f'window.scrollTo(0, -{num_pixels})')

    def scroll_down(self, num_pixels):
        self._driver.execute_script(f'window.scrollTo(0, {num_pixels})')

    def scroll_to_top(self):
        self._driver.execute_script(f'window.scrollTo(0, -document.body.scrollHeight)')

    def scroll_to_bottom(self):
        self._driver.execute_script(f'window.scrollTo(0, document.body.scrollHeight)')

    def scroll_left(self, num_pixels):
        self._driver.execute_script(f'window.scrollLeft({num_pixels}, 0)')

    def scroll_into_view_if_needed(self, element):
        self._driver.execute_script('arguments[0].scrollIntoViewIfNeeded(true);', element)

    def wait_for_js_to_load(self):
        self._wait.until(lambda _driver: _driver.execute_script('return document.readyState') == 'complete')

    def wait_for_jquery_to_load(self):
        self._wait.until(lambda _driver: _driver.execute_script('return jQuery.active == 0'))

    def wait_for_js_and_jquery_to_load(self):
        self.wait_for_js_to_load()
        self.wait_for_jquery_to_load()

    # Window handlers
    def open_dialog(self, locator):
        # Store the id of original window
        original_window = self._driver.current_window_handle
        # Check number of current window = 1
        assert len(self._driver.window_handles) == 1
        # Click to open new window
        self.click(locator)
        # Wait until number of windows = 2
        self._wait.until(EC.number_of_windows_to_be(2))
        # For loop to find new window 
        for window_handle in self._driver.window_handles:
            if window_handle != original_window:
                # Switch to new window
                self._driver.switch_to.new_window(window_handle)
                break

    def open_alert(self, locator):
        self.click(locator)
        # self._wait.until(EC.alert_is_present())
        # alert = self._driver.switch_to.alert
        # print(alert)


    # NAVIGATION
    def navigate_to(self, url):
        url = url.lower()
        if not url.startswith(('http', 'https')):
            if url is None or url == '/':
                url = BASE_URL
            else:
                url = BASE_URL + url
        
        self._driver.get(url)

    def view_product(self, product):
        self.navigate_to(product['slug'])

    def view_category(self, category_name):
        self.navigate_to(category_name)

    def refresh_page(self):
        self._driver.refresh()

    def go_back(self):
        self._driver.back()

    def go_forward(self):
        self._driver.forward()

    # ASSERTION
    def assert_true(condition_func, failure_msg=None):
        assert condition_func, failure_msg

    def assert_false(condition_func, failure_msg=None):
        assert condition_func == False, failure_msg
    
    def verify(self, actual, expected=True):
        if expected == actual:
            # add log here
            pass
        else:
            # add log here
            self.take_screenshot()
        
        assert expected == actual, f'Expected result: {expected}, but actual: {actual}'

    def assert_in(self, value, source):
        assert value in source, f'Expected {value} in {source} but actual is not'

    def expect_title(self, text):
        self.verify(self._driver.title, text)

    def expect_title_contains(self, text):
        self.assert_in(text, self._driver.title)
    
    def expect_url(self, text):
        self.verify(self._driver.current_url, text)
    
    def expect_url_contains(self, text):
        self.assert_in(text, self._driver.current_url)
    
    def expect_contain_text(self, locator, text):
        ele_txt = self.get_element_text(locator)
        self.assert_in(text, ele_txt)
    
    def take_screenshot(self):
        """
        screenshot file name should be: 'current_dt_TC_id...' 
        but for now, add current datetime only
        """
        datetime_fmt = '%Y-%m-%d_at_%H-%M-%S'
        current_dt = datetime.now().strftime(datetime_fmt)
        current_dir = Path.cwd()
        screenshots_dir = Path.joinpath(current_dir, 'screenshots')
        file_name = current_dt + '.png'
        destination_file = Path.joinpath(screenshots_dir, file_name)
        try:
            self._driver.save_screenshot(destination_file)
        except:
            print('Oops! Something went wrong when trying to take a screenshot')