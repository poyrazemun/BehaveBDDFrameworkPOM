from features.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_input_xpath = "//input[@name='firstname']"
    last_name_input_xpath = "//input[@name='lastname']"
    email_input_xpath = "//input[@name='email']"
    telephone_input_xpath = "//input[@name='telephone']"
    password_input_xpath = "//input[@name='password']"
    password_confirm_input_xpath = "//input[@name='confirm']"
    privacy_policy_checkbox_xpath = "//input[@name='agree']"

    continue_button_xpath = "//input[@value='Continue']"

    duplicate_email_warning_message_xpath = "//div[text()='Warning: E-Mail Address is already registered!']"

    expected_privacy_warning_xpath = "//div[text()='Warning: You must agree to the Privacy Policy!']"
    expected_first_name_warning_xpath = "//div[text()='First Name must be between 1 and 32 characters!']"
    expected_last_name_warning_xpath = "//div[text()='Last Name must be between 1 and 32 characters!']"
    expected_email_address_warning_xpath = "//div[text()='E-Mail Address does not appear to be valid!']"
    expected_telephone_warning_xpath = "//div[text()='Telephone must be between 3 and 32 characters!']"
    expected_password_warning_xpath = "//div[text()='Password must be between 4 and 20 characters!']"

    def enter_first_name(self, first_name):
        self.element_send_keys(first_name, self.first_name_input_xpath)

    def enter_last_name(self, last_name):
        self.element_send_keys(last_name, self.last_name_input_xpath)

    def enter_email(self, email=""):
        self.element_send_keys(email, self.email_input_xpath)

    def enter_telephone_number(self, tel_num):
        self.element_send_keys(tel_num, self.telephone_input_xpath)

    def enter_password(self, password):
        self.element_send_keys(password, self.password_input_xpath)

    def enter_password_to_confirm(self, password):
        self.element_send_keys(password, self.password_confirm_input_xpath)

    def fill_out_the_mandatory_fields(self, first_name="", last_name="", email="", tel_num="", password=""):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_telephone_number(tel_num)
        self.enter_password(password)
        self.enter_password_to_confirm(password)

    def click_on_privacy_policy_option_checkbox(self):
        self.element_click(locator=self.privacy_policy_checkbox_xpath)

    def click_on_continue_button(self):
        self.element_click(locator=self.continue_button_xpath)

    def verify_warning_displayed_for_duplicate_email(self):
        return self.is_element_displayed(locator=self.duplicate_email_warning_message_xpath)

    def verify_expected_privacy_warning_message_is_displayed(self):
        return self.is_element_displayed(locator=self.expected_privacy_warning_xpath)

    def verify_expected_first_name_warning_message_is_displayed(self):
        return self.is_element_displayed(locator=self.expected_first_name_warning_xpath)

    def verify_expected_last_name_warning_message_is_displayed(self):
        return self.is_element_displayed(locator=self.expected_last_name_warning_xpath)

    def verify_expected_email_address_warning_message_is_displayed(self):
        return self.is_element_displayed(locator=self.expected_email_address_warning_xpath)

    def verify_expected_tel_warning_message_is_displayed(self):
        return self.is_element_displayed(locator=self.expected_telephone_warning_xpath)

    def verify_expected_password_warning_message_is_displayed(self):
        return self.is_element_displayed(locator=self.expected_password_warning_xpath)

    def verify_messages_for_every_mandatory_field_is_displayed(self):
        return all([
            self.verify_expected_privacy_warning_message_is_displayed(),
            self.verify_expected_first_name_warning_message_is_displayed(),
            self.verify_expected_last_name_warning_message_is_displayed(),
            self.verify_expected_email_address_warning_message_is_displayed(),
            self.verify_expected_tel_warning_message_is_displayed(),
            self.verify_expected_password_warning_message_is_displayed()
        ])

        # all() fonksiyonu, verilen iterable (örneğin bir liste) içindeki tüm elemanlar True ise True döndürür,
        # herhangi bir eleman False ise False döndürür.
