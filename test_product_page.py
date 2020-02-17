from pages.main_page import ProductPage
import pytest
from pages.main_page import LoginPage
import time



class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@ololo.org"
        password = "ololololo"
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = LoginPage(browser, self.link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        self.page.open()  # открываем страницу
        self.page.go_to_login_page()
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()


    def test_user_can_add_product_to_basket(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, self.link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        self.page.open()
        self.page.add_product_to_basket()
        #self.page.solve_quiz_and_get_code()
        self.page.should_be_name_in_mesage()
        self.page.should_be_price_i_masage()


    def test_user_cant_see_success_message(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, self.link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        self.page.open()
        self.page.should_be_success_message_after_adding_product_to_basket()

'''def test_guest_can_go_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_be_promo_in_url()'''

'''@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message_after_adding_product_to_basket()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_product_to_basket()
    page.should_be_message_disappeared_after_adding_product_to_basket()'''
'''def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()'''