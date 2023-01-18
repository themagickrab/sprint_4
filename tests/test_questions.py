import allure
import pytest
from pages.main_page import MainPage

@allure.title("Тесты ответов")
@pytest.mark.parametrize('quest, answer, text_answer',
[(MainPage.QUESTION_ONE, MainPage.ANSWER_ONE_TEXT, MainPage.text_answer_1),
 (MainPage.QUESTION_TWO, MainPage.ANSWER_TWO_TEXT, MainPage.text_answer_2),
 (MainPage.QUESTION_THREE, MainPage.ANSWER_THREE_TEXT, MainPage.text_answer_3),
 (MainPage.QUESTION_FOUR, MainPage.ANSWER_FOUR_TEXT, MainPage.text_answer_4),
 (MainPage.QUESTION_FIVE, MainPage.ANSWER_FIVE_TEXT, MainPage.text_answer_5),
 (MainPage.QUESTION_SIX, MainPage.ANSWER_SIX_TEXT, MainPage.text_answer_6),
 (MainPage.QUESTION_SEVEN, MainPage.ANSWER_SEVEN_TEXT, MainPage.text_answer_7),
 (MainPage.QUESTION_EIGHT, MainPage.ANSWER_EIGHT_TEXT, MainPage.text_answer_8)])
def test_answers(driver, quest, answer, text_answer):
    main = MainPage(driver)
    text = main.get_text_answer(quest, answer)
    assert text_answer == text