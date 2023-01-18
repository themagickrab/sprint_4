import allure
from pages.main_page import MainPage

@allure.title('Проверяем тескт ответа на вопрос - "Сколько это стоит? И как оплатить?"')
def test_answer_one(driver):
    main = MainPage(driver)
    main.scroll_to_questions()
    main.click_question_one()
    text = main.get_text_answer_one()
    text_q = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    assert text_q == text

@allure.title('Проверяем тескт ответа на вопрос - "Хочу сразу несколько самокатов! Так можно?"')
def test_answer_two(driver):
    main = MainPage(driver)
    main.scroll_to_questions()
    main.click_question_two()
    text = main.get_text_answer_two()
    text_q = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, ' \
             'можете просто сделать несколько заказов — один за другим.'
    assert text_q == text

@allure.title('Проверяем тескт ответа на вопрос - "Как рассчитывается время аренды?"')
def test_answer_three(driver):
    main = MainPage(driver)
    main.scroll_to_questions()
    main.click_question_three()
    text = main.get_text_answer_three()
    text_q = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
             'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
             'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    assert text_q == text

@allure.title('Проверяем тескт ответа на вопрос - "Можно ли заказать самокат прямо на сегодня?"')
def test_answer_four(driver):
    main = MainPage(driver)
    main.scroll_to_questions()
    main.click_question_four()
    text = main.get_text_answer_four()
    text_q = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    assert text_q == text

@allure.title('Проверяем тескт ответа на вопрос - "Можно ли продлить заказ или вернуть самокат раньше?"')
def test_answer_five(driver):
    main = MainPage(driver)
    main.scroll_to_questions()
    main.click_question_five()
    text = main.get_text_answer_five()
    text_q = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    assert text_q == text

@allure.title('Проверяем тескт ответа на вопрос - "Вы привозите зарядку вместе с самокатом?"')
def test_answer_six(driver):
    main = MainPage(driver)
    main.scroll_to_questions()
    main.click_question_six()
    text = main.get_text_answer_six()
    text_q = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься ' \
             'без передышек и во сне. Зарядка не понадобится.'
    assert text_q == text

@allure.title('Проверяем тескт ответа на вопрос - "Можно ли отменить заказ?"')
def test_answer_seven(driver):
    main = MainPage(driver)
    main.scroll_to_questions()
    main.click_question_seven()
    text = main.get_text_answer_seven()
    text_q = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    assert text_q == text

@allure.title('Проверяем тескт ответа на вопрос - "Я живу за МКАДом, привезёте?"')
def test_answer_eight(driver):
    main = MainPage(driver)
    main.scroll_to_questions()
    main.click_question_eight()
    text = main.get_text_answer_eight()
    text_q = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    assert text_q == text