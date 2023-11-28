from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "Message about empty basket did not present"

