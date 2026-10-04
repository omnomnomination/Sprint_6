import pytest
import allure 
from pages.order_page import OrderPage

class TestOrderPage:
    @allure.title("Позитивный флоу заказа самоката через кнопку {button_type}")
    @pytest.mark.parametrize(
        "button_type, first_name, last_name, address, metro, phone, date, duration, color, comment",
        [
            ("top", "Олег", "Тиньков", "Москва", "Сокольники", "88888888888", "10.10.2026", "семеро суток", "grey", "+++"),
            ("bottom", "Мария", "Кюри", "Санкт-Петербург", "Черкизовская", "77777777777", "25.10.2026", "трое суток", "black", "---")
        ]
    )

    def test_order_flow(self, driver, button_type, first_name, last_name, address, metro, phone, date, duration, color, comment):
        order_page = OrderPage(driver)
        order_page.open()
        
        order_page.click_order_button(button_type)
        order_page.fill_first_form(first_name, last_name, address, metro, phone)
        order_page.fill_second_form(date, duration, color, comment)
        
        assert order_page.is_order_successful()

    @allure.title("Проверка перехода на стартовую страницу при нажатии на логотип самоката")
    def test_logo_scooter_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_top_order_button()
        order_page.click_scooter_logo()
        assert order_page.get_current_url() == order_page.base_url
    
    @allure.title("Проверка перехода в дзен при нажатии на логотип яндекса")
    def test_logo_yandex_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_yandex_logo()
        current_url = order_page.switch_to_new_window_and_get_url()
        assert "dzen.ru" in current_url
