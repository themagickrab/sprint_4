from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
class WhoIsTheScooterFor(BasePage):
    NAME_FIELD = [By.CSS_SELECTOR, '[placeholder="* Имя"]']
    LAST_NAME_FIELD = [By.CSS_SELECTOR, '[placeholder="* Фамилия"]']
    ADDRESS_FIELD = [By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]']
    METRO_STATION_FIELD = [By.CSS_SELECTOR, '[placeholder="* Станция метро"]']
    PHONE_FIELD = [By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, '//*[text()="Далее"]']
    PLACEHOLDER_METRO_BUTTON = [By.CLASS_NAME, 'select-search__select']

    def set_name(self, name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def set_metro(self, metro):
        self.driver.find_element(*self.METRO_STATION_FIELD).send_keys(metro)
        self.driver.find_element(*self.PLACEHOLDER_METRO_BUTTON).click()

    def set_phone(self, phone):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.PHONE_FIELD))
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    def click_next(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.NEXT_BUTTON))
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def filling_in_personal_data(self, name, last_name,address, metro, phone):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_next()








