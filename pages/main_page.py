from pages.base_page import BasePage
from locators.locators_start_page import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def scroll_to_faq(self):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        formatted_locator = (method, locator.format(0))
        self.scroll_to_element(formatted_locator)

    def click_question(self, index):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        formatted_locator = (method, locator.format(index))
        self.click_element(formatted_locator)

    def get_answer_text(self, index):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        formatted_locator = (method, locator.format(index))
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(formatted_locator)
        )
        return element.text
