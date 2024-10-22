from features.pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    expected_message_for_invalid_search = "There is no product that matches the search criteria."
    message_for_invalid_search_xpath = "//input[@id='button-search']/following-sibling::p"

    def get_valid_product_xpath(self, product):
        return f"//a[contains(text(),'{product}')]"

    def verify_valid_product_displayed(self, product):
        valid_product_xpath = self.get_valid_product_xpath(product)
        result = self.is_element_displayed(locator=valid_product_xpath)
        return result

    def verify_proper_message_displayed_for_invalid_product(self):
        actual_message = self.get_text(locator=self.message_for_invalid_search_xpath)
        return self.expected_message_for_invalid_search == actual_message
