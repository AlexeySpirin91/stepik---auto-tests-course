from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "login not in current url"# реализуйте проверку на корректный url адре

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "Login email input is not presented"# реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "Login password input is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM_EMAIL), "Reg email input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_FORM_PASSWORD1), "Reg password1 input is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_FORM_PASSWORD2), "Reg password2 input is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
