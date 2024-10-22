from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import utilities.custom_logger as cl
import time
import os
import logging


class SeleniumDriver:
    log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, result_message):
        file_name = f"{result_message}_{time.strftime('%Y%m%d_%H%M%S')}.png"
        screenshots_directory = "../screenshots/"
        relative_file_name = screenshots_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshots_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved into: " + destination_file)
        except:
            self.log.error("Exception occurred.")

    def get_title(self):
        return self.driver.title

    def get_the_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="xpath"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_the_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            # self.log.info("Element is found with this locator: " + str(locator))
        except NoSuchElementException:
            self.log.error("Element not found")
        return element

    def select_from_dropdown(self, locator, visible_text, locator_type="xpath"):
        try:
            dropdown_element = self.get_element(locator, locator_type)
            select = Select(dropdown_element)
            select.select_by_visible_text(visible_text)
            self.log.info(f"'{visible_text}' is chosen.")
        except NoSuchElementException:
            self.log.error(f"Dropdown element cant be found: {locator}")

    def get_element_list(self, locator, locator_type="xpath"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_the_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def element_click(self, locator="", locator_type="xpath", element=None):
        try:
            if element is None:
                element = self.wait_for_element_to_be_clickable(locator, locator_type)
            if element is not None:
                element.click()
        except StaleElementReferenceException:
            self.log.error("StaleElementReferenceException: The element is no longer attached to the DOM.")
            element = self.wait_for_element_to_be_clickable(locator, locator_type)  # Elementi yeniden bul
            element.click()  # Tekrar tıkla
            self.log.info("Element is attached to the DOM and is found!.")
        except:
            self.log.error("Errrrrrooooooooor!")
            print_stack()

    def element_send_keys(self, data, locator="", locator_type="xpath", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            self.element_click(element)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def get_text(self, locator="", locator_type="xpath", element=None, info=""):

        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()

        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locator_type="xpath", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            print("Element not found")
            return False

    def is_element_displayed(self, locator=None, locator_type="xpath", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_displayed = False
        try:
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed directly.")
            elif locator:
                element = self.get_element(locator, locator_type)
                if element is not None:
                    is_displayed = element.is_displayed()
                    self.log.info("Element is displayed with locator: " + locator +
                                  " locatorType: " + locator_type)
                else:
                    self.log.error("Element not displayed with locator: " + locator +
                                   " locatorType: " + locator_type)
            else:
                self.log.error("No element or locator provided.")
            return is_displayed
        except Exception as e:
            self.log.error(f"Exception occurred: {e}")
            return False

    def wait_for_element(self, locator, locator_type, timeout=10):
        element = None
        try:
            by_type = self.get_the_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout, ignored_exceptions=[NoSuchElementException,
                                                                           ElementNotSelectableException,
                                                                           StaleElementReferenceException,
                                                                           ElementClickInterceptedException])

            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            # self.log.info("Element appeared on the web page.")
        except:
            self.log.info("Element not appeared on the web page!")
            print_stack()
        return element

    def wait_for_element_to_be_clickable(self, locator, locator_type, timeout=10):
        element = None
        try:
            by_type = self.get_the_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, ignored_exceptions=[NoSuchElementException,
                                                                           ElementNotSelectableException,
                                                                           StaleElementReferenceException,
                                                                           ElementClickInterceptedException])

            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            # self.log.info("Element appeared on the web page.")
        except:
            self.log.info("Element not appeared on the web page!")
            print_stack()
        return element

    def scroll(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def switch_iframe_by_index(self, locator, locator_type="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.get_element_list("//iframe", locator_type="xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.driver.switch_to.frame(index=iframe_list[i])
                result = self.is_element_present(locator, locator_type)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.driver.switch_to.default_content()
            return result
        except:
            print("iFrame index not found")
            return result
