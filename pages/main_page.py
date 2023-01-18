from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class MainPage(BasePage):
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

    text_answer_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    text_answer_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '\
             'можете просто сделать несколько заказов — один за другим.'
    text_answer_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
             'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
             'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    text_answer_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    text_answer_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    text_answer_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься ' \
             'без передышек и во сне. Зарядка не понадобится.'
    text_answer_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    text_answer_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


    def scroll_to_order_button(self):
        element = self.driver.find_element(*self.ORDER_BUTTON_ON_MAIN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_order_button_on_main(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.ORDER_BUTTON_ON_MAIN))
        self.driver.find_element(*self.ORDER_BUTTON_ON_MAIN).click()

    def get_text_answer(self, quest,answer):
        fq = self.driver.find_element(*self.FAQ_TABLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", fq)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(quest))
        self.driver.find_element(*quest).click()
        text = self.driver.find_element(*answer).text
        return text
