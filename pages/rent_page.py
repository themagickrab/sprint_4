from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class RentPage(BasePage):
    CALENDAR_FIELD = [By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]']
    RENTAL_PERIOD_FIELD = [By.CLASS_NAME, 'Dropdown-placeholder']
    DROPDOWN_MENU = [By.XPATH, '//*[text()="трое суток"]']
    ORDER_BUTTON_ON_ORDER_PAGE = [By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    BUTTON_YES = [By.XPATH, '//*[text()="Да"]']
    BUTTON_VIEW_STATUS = [By.XPATH, '//*[text()="Посмотреть статус"]']

    def set_calendar(self, date):
        self.driver.find_element(*self.CALENDAR_FIELD).send_keys(date)
        self.driver.find_element(*self.CALENDAR_FIELD).send_keys(Keys.ESCAPE)

    def set_rental_period(self):
        self.driver.find_element(*self.RENTAL_PERIOD_FIELD).click()
        self.driver.find_element(*self.DROPDOWN_MENU).click()

    def click_order_button_on_order_page(self):
        self.driver.find_element(*self.ORDER_BUTTON_ON_ORDER_PAGE).click()

    def click_button_yes(self):
        self.driver.find_element(*self.BUTTON_YES).click()

    def receive_text_view_status_button(self):
        text = self.driver.find_element(*self.BUTTON_VIEW_STATUS).text
        return text

    def click_on_view_status_button(self):
        self.driver.find_element(*self.BUTTON_VIEW_STATUS).click()

    def filling_order_date(self, date):
        self.set_calendar(date)
        self.set_rental_period()
        self.click_order_button_on_order_page()
        self.click_button_yes()









