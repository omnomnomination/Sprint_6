from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = (By.ID, 'accordion__heading-{}')
    ANSWER_LOCATOR = (By.ID, 'accordion__panel-{}')
