from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo_in_url(self):
        self.promo_url = self.browser.current_url
        assert "?promo=newYear" in self.promo_url, 'no promo in url'

    def add_product_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button add is not presented"
        button_add.click()
    def should_be_name_in_mesage(self):
        self.button_add_title = self.browser.find_element(*ProductPageLocators.TITLE_BOOK)
        self.button_text = self.button_add_title.text
        self.mesage_el = self.browser.find_element(*ProductPageLocators.NAME)
        self.mesage = self.mesage_el.text
        assert self.button_text == self.mesage, 'no title in mesage'

    def should_be_price_i_masage(self):
        self.prise_el = self.browser.find_element(*ProductPageLocators.PRISE)
        self.prise = self.prise_el.text
        self.prise_in_basket_el = self.browser.find_element(*ProductPageLocators.PRISE_IN_BASKET)
        self.prise_in_basket = self.prise_in_basket_el.text
        assert self.button_text in self.mesage, 'price'

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME), 'message on page'

    def should_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME), 'no message'

    def should_be_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.NAME), 'message on page'
