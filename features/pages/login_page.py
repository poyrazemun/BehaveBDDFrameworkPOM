from features.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_input_xpath = "//input[@id='input-email']"
    password_input_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"
    warning_for_failed_login_message_xpath = "//div[text()='Warning: No match for E-Mail Address and/or Password.']"

    def enter_email(self, email):
        self.element_send_keys(email, self.email_input_xpath)

    def enter_password(self, password):
        self.element_send_keys(password, self.password_input_xpath)

    def click_login_button(self):
        self.element_click(locator=self.login_button_xpath)

    def verify_login_is_failed(self):
        result = self.is_element_displayed(locator=self.warning_for_failed_login_message_xpath)
        return result
