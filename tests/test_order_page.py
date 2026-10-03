import pytest
from pages.order_page import OrderPage

@pytest.mark.parametrize(
    "button_type, first_name, last_name, address, metro, phone, date, duration, color, comment",
    [
        ("top", "Олег", "Тиньков", "Москва", "Сокольники", "88888888888", "10.10.2026", "семеро суток", "grey", "+++"),
        ("bottom", "Мария", "Кюри", "Санкт-Петербург", "Черкизовская", "77777777777", "25.10.2026", "трое суток", "black", "---")
    ]
)
def test_order_flow(driver, button_type, first_name, last_name, address, metro, phone, date, duration, color, comment):
    order_page = OrderPage(driver)
    order_page.open()
    
    if button_type == "top":
        order_page.click_top_order_button()
    else:
        order_page.click_bottom_order_button()
        
    order_page.fill_first_form(first_name, last_name, address, metro, phone)
    order_page.fill_second_form(date, duration, color, comment)
    
    assert order_page.is_order_successful()

def test_logo_scooter_redirect(driver):
    order_page = OrderPage(driver)
    order_page.open()
    order_page.click_top_order_button()
    order_page.click_scooter_logo()
    assert driver.current_url == order_page.base_url

def test_logo_yandex_redirect(driver):
    order_page = OrderPage(driver)
    order_page.open()
    order_page.click_yandex_logo()
    current_url = order_page.switch_to_new_window_and_get_url()
    assert "dzen.ru" in current_url
