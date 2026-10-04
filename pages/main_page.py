from pages.base_page import BasePage
from locators.locators_start_page import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPage(BasePage):
    @allure.step("Пролистываем страницу до выпадающего списка FAQ")
    def scroll_to_faq(self):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        formatted_locator = (method, locator.format(0))
        self.scroll_to_element(formatted_locator)

    @allure.step("Клик по вопросу №{index}")
    def click_question(self, index):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        formatted_locator = (method, locator.format(index))
        self.click_element(formatted_locator)

    @allure.step("Получить текст ответа №{index}")
    def get_answer_text(self, index):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        formatted_locator = (method, locator.format(index))
        element = self.wait_for_visibility(formatted_locator)
        return element.text
