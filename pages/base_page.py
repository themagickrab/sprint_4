from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    LOGO_YANDEX = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    LOGO_SCOOTER = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    ORDER_BUTTON_IN_HEADER = [By.CLASS_NAME, 'Button_Button__ra12g']
    ORDER_STATUS_BUTTON = [By.CLASS_NAME, 'Header_Link__1TAG7']
    COOKIE_BUTTON = [By.ID, 'rcc-confirm-button']
    TAB = 'https://dzen.ru/?yredirect=true'

    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex(self):
        self.driver.find_element(*self.LOGO_YANDEX).click()

    def click_logo_scotter(self):
        self.driver.find_element(*self.LOGO_SCOOTER).click()

    def click_order_button_in_header(self):
        self.driver.find_element(*self.ORDER_BUTTON_IN_HEADER).click()

    def click_order_status_button(self):
        self.driver.find_element(*self.ORDER_STATUS_BUTTON).click()

    def wait_for_order_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(*self.ORDER_BUTTON_IN_HEADER))

    def click_cookie_button(self):
        self.driver.find_element(*self.COOKIE_BUTTON).click()

    def get_url(self):
        url = self.driver.current_url
        return url

    def wait_new_tab(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'))

    def switch_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


