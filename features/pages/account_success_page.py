from features.pages.base_page import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    account_is_created_verifier_xpath = "//div[@id='content']//h1[text()='Your Account Has Been Created!']"

    def verify_account_creation(self):
        return self.is_element_displayed(locator=self.account_is_created_verifier_xpath)
