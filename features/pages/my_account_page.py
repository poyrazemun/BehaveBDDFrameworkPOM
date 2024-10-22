from features.pages.base_page import BasePage


class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    login_successful_verifier_xpath = "//div[@id='content']//h2[text()='My Account']"

    def verify_login_is_successful(self):
        result = self.is_element_displayed(locator=self.login_successful_verifier_xpath)
        return result
