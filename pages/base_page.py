from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

BASE_URL = "https://qa-scooter.praktikum-services.ru/"

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    @allure.step("Открыть стартовую страницу")
    def open(self):
        self.driver.get(self.base_url)
    
    @allure.step("Ожидание появления элемента и клик по нему")
    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    @allure.step("Скролл до нужного элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание видимости элемента")
    def wait_for_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

