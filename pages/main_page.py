from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPage:
    ORDER_BUTTON_ON_MAIN = [By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button']
    FAQ_TABLE = [By.CLASS_NAME, 'Home_FAQ__3uVm4']

    QUESTION_ONE = [By.ID, 'accordion__heading-0']
    QUESTION_TWO = [By.ID, 'accordion__heading-1']
    QUESTION_THREE = [By.ID, 'accordion__heading-2']
    QUESTION_FOUR = [By.ID, 'accordion__heading-3']
    QUESTION_FIVE = [By.ID, 'accordion__heading-4']
    QUESTION_SIX = [By.ID, 'accordion__heading-5']
    QUESTION_SEVEN = [By.ID, 'accordion__heading-6']
    QUESTION_EIGHT = [By.ID, 'accordion__heading-7']

    ANSWER_ONE_TEXT = [By.XPATH, '//*[@id="accordion__panel-0"]']
    ANSWER_TWO_TEXT = [By.XPATH, '//*[@id="accordion__panel-1"]']
    ANSWER_THREE_TEXT = [By.XPATH, '//*[@id="accordion__panel-2"]']
    ANSWER_FOUR_TEXT = [By.XPATH, '//*[@id="accordion__panel-3"]']
    ANSWER_FIVE_TEXT = [By.XPATH, '//*[@id="accordion__panel-4"]']
    ANSWER_SIX_TEXT = [By.XPATH, '//*[@id="accordion__panel-5"]']
    ANSWER_SEVEN_TEXT = [By.XPATH, '//*[@id="accordion__panel-6"]']
    ANSWER_EIGHT_TEXT = [By.XPATH, '//*[@id="accordion__panel-7"]']

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_order_button(self):
        element = self.driver.find_element(*self.ORDER_BUTTON_ON_MAIN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_order_button_on_main(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ORDER_BUTTON_ON_MAIN))
        self.driver.find_element(*self.ORDER_BUTTON_ON_MAIN).click()

    def scroll_to_questions(self):
        fq = self.driver.find_element(*self.FAQ_TABLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", fq)

    def click_question_one(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.QUESTION_ONE))
        self.driver.find_element(*self.QUESTION_ONE).click()

    def get_text_answer_one(self):
        text = self.driver.find_element(*self.ANSWER_ONE_TEXT).text
        return text

    def click_question_two(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.QUESTION_TWO))
        self.driver.find_element(*self.QUESTION_TWO).click()

    def get_text_answer_two(self):
        text = self.driver.find_element(*self.ANSWER_TWO_TEXT).text
        return text

    def click_question_three(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.QUESTION_THREE))
        self.driver.find_element(*self.QUESTION_THREE).click()

    def get_text_answer_three(self):
        text = self.driver.find_element(*self.ANSWER_THREE_TEXT).text
        return text

    def click_question_four(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.QUESTION_FOUR))
        self.driver.find_element(*self.QUESTION_FOUR).click()

    def get_text_answer_four(self):
        text = self.driver.find_element(*self.ANSWER_FOUR_TEXT).text
        return text

    def click_question_five(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.QUESTION_FIVE))
        self.driver.find_element(*self.QUESTION_FIVE).click()

    def get_text_answer_five(self):
        text = self.driver.find_element(*self.ANSWER_FIVE_TEXT).text
        return text

    def click_question_six(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.QUESTION_SIX))
        self.driver.find_element(*self.QUESTION_SIX).click()

    def get_text_answer_six(self):
        text = self.driver.find_element(*self.ANSWER_SIX_TEXT).text
        return text

    def click_question_seven(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.QUESTION_SEVEN))
        self.driver.find_element(*self.QUESTION_SEVEN).click()

    def get_text_answer_seven(self):
        text = self.driver.find_element(*self.ANSWER_SEVEN_TEXT).text
        return text

    def click_question_eight(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.QUESTION_EIGHT))
        self.driver.find_element(*self.QUESTION_EIGHT).click()

    def get_text_answer_eight(self):
        text = self.driver.find_element(*self.ANSWER_EIGHT_TEXT).text
        return text