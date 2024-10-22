from features.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    my_account_xpath = "//span[text()='My Account']"
    login_option_xpath = "//a[text()='Login']"
    register_option_xpath = "//a[text()='Register']"
    expected_title = "Your Store"
    search_box_xpath = "//input[@name='search']"
    search_button_xpath = "//div[@id='search']//button"

    def click_on_my_account(self):
        self.element_click(locator=self.my_account_xpath, locator_type="xpath")

    def click_on_login_option(self):
        self.element_click(locator=self.login_option_xpath)

    def click_on_register_option(self):
        self.element_click(locator=self.register_option_xpath)

    def verify_navigation_to_home_page(self):
        result = self.verify_page_title(self.expected_title)
        return result

    def type_into_search_box(self, text):
        self.element_send_keys(text, locator=self.search_box_xpath)

    def click_on_search_button(self):
        self.element_click(locator=self.search_button_xpath)
