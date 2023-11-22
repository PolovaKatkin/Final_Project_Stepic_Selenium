from base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка на корректный url адрес
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "The URL is not correct"

    # Проверка, что форма входа есть на странице
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.ENTER_ADDRESS), "The login form was not found"

    # Проверка, что форма регистрации есть на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_ADDRESS), "The registration form was not found"
