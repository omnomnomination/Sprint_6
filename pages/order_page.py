from pages.base_page import BasePage
from locators.locators_order_page import OrderPageLocators
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage(BasePage):

    @allure.step("Кликнуть верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(OrderPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Кликнуть нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать на кнопку заказа типа {button_type}")
    def click_order_button(self, button_type):
        if button_type == "top":
            self.click_top_order_button()
        else:
            self.click_bottom_order_button()

    @allure.step("Заполняем первую форму")
    def fill_first_form(self, first_name, last_name, address, metro_station, phone):
        self.send_keys_to_element(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys_to_element(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        method, locator = OrderPageLocators.METRO_OPTION_TEMPLATE
        formatted_metro = (method, locator.format(metro_station))
        self.click_element(formatted_metro)
        
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем вторую форму")
    def fill_second_form(self, date, duration, color_id, comment):
        self.send_keys_to_element(OrderPageLocators.DATE_INPUT, date)
        
        date_field = self.wait_for_visibility(OrderPageLocators.DATE_INPUT)
        date_field.send_keys(Keys.ENTER)
        
        self.click_element(OrderPageLocators.RENT_DURATION_DROPDOWN)
        method_dur, locator_dur = OrderPageLocators.RENT_DURATION_OPTION_TEMPLATE
        formatted_dur = (method_dur, locator_dur.format(duration))
        self.click_element(formatted_dur)
        
        method_col, locator_col = OrderPageLocators.COLOR_CHECKBOX_TEMPLATE
        formatted_col = (method_col, locator_col.format(color_id))
        self.click_element(formatted_col)
        
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_element(OrderPageLocators.FINAL_ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Получаем подтверждение, что заказ сформирован")
    def is_order_successful(self):
        element = self.wait_for_visibility(OrderPageLocators.SUCCESS_ORDER_HEADER)
        return element.is_displayed()

    @allure.step("Нажимаем на логотип сервиса Самокат")
    def click_scooter_logo(self):
        self.click_element(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Нажимаем на логотип сервиса Яндекс")
    def click_yandex_logo(self):
        self.click_element(OrderPageLocators.YANDEX_LOGO)

    @allure.step("Получаем подтверждение, что совершен переход на нужную страницу")
    def switch_to_new_window_and_get_url(self):
        return self.get_new_window_url("dzen.ru")
