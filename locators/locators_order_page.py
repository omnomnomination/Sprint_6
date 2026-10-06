from selenium.webdriver.common.by import By

class OrderPageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, 'Button_Middle')]")
    
    FIRST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_OPTION_TEMPLATE = (By.XPATH, ".//li[@class='select-search__row' and .//div[text()='{}']]")
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_DURATION_DROPDOWN = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    RENT_DURATION_OPTION_TEMPLATE = (By.XPATH, ".//div[@class='Dropdown-option' and text()='{}']")
    COLOR_CHECKBOX_TEMPLATE = (By.XPATH, ".//label[@for='{}']")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    FINAL_ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать' and contains(@class, 'Button_Middle')]")
    
    CONFIRM_YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_ORDER_HEADER = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")

