from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.util = Util()

    def verify_page_title(self, title_to_verify):
        """
        Verify the page Title

        Parameters:
            title_to_verify: Title on the page that needs to be verified
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_match(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            return False
