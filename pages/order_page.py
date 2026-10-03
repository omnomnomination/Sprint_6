from pages.base_page import BasePage
from locators.locators_order_page import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    def click_top_order_button(self):
        self.click_element(OrderPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.scroll_to_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(OrderPageLocators.BOTTOM_ORDER_BUTTON)

    def fill_first_form(self, first_name, last_name, address, metro_station, phone):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.FIRST_NAME_INPUT)).send_keys(first_name)
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        method, locator = OrderPageLocators.METRO_OPTION_TEMPLATE
        formatted_metro = (method, locator.format(metro_station))
        self.click_element(formatted_metro)
        
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, date, duration, color_id, comment):
        date_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT))
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        
        self.click_element(OrderPageLocators.RENT_DURATION_DROPDOWN)
        method_dur, locator_dur = OrderPageLocators.RENT_DURATION_OPTION_TEMPLATE
        formatted_dur = (method_dur, locator_dur.format(duration))
        self.click_element(formatted_dur)
        
        method_col, locator_col = OrderPageLocators.COLOR_CHECKBOX_TEMPLATE
        formatted_col = (method_col, locator_col.format(color_id))
        self.click_element(formatted_col)
        
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        self.click_element(OrderPageLocators.FINAL_ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)


    def is_order_successful(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_ORDER_HEADER)
        )
        return element.is_displayed()

    def click_scooter_logo(self):
        self.click_element(OrderPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(OrderPageLocators.YANDEX_LOGO)

    def switch_to_new_window_and_get_url(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(lambda d: "dzen.ru" in d.current_url)
        return self.driver.current_url
