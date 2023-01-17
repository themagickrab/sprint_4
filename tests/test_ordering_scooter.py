import allure
from confest import personal_data, personal_data_two, date, driver
from pages.base_page import BasePage
from pages.whom_scooter_page import WhoIsTheScooterFor
from pages.rent_page import RentPage
from pages.main_page import MainPage

driver = driver
personal_data = personal_data
personal_data_two = personal_data_two
date = date

@allure.title('Тест аренды скутера через кнопку "заказать" в шапке')
def test_ordering_scooter_via_the_order_button_in_the_header(driver, personal_data, date):
    name = personal_data.get('name')
    last_name = personal_data.get('last_name')
    address = personal_data.get('address')
    metro = personal_data.get('metro')
    phone = personal_data.get('phone')
    base_page = BasePage(driver)
    base_page.click_cookie_button()
    base_page.click_order_button_in_header()
    scooter_page = WhoIsTheScooterFor(driver)
    scooter_page.filling_in_personal_data(name, last_name, address, metro, phone)
    rent_page = RentPage(driver)
    rent_page.filling_order_date(date)
    text = rent_page.receive_text_view_status_button()
    text_button = 'Посмотреть статус'
    assert text_button == text

@allure.title('Тест аренды скутера через кнопку "заказать" на главной')
def test_ordering_scooter_via_the_order_button_in_main_page(driver, personal_data_two, date):
    name = personal_data_two.get('name')
    last_name = personal_data_two.get('last_name')
    address = personal_data_two.get('address')
    metro = personal_data_two.get('metro')
    phone = personal_data_two.get('phone')
    base_page = BasePage(driver)
    base_page.click_cookie_button()
    main_page = MainPage(driver)
    main_page.scroll_to_order_button()
    main_page.click_order_button_on_main()
    scooter_page = WhoIsTheScooterFor(driver)
    scooter_page.filling_in_personal_data(name, last_name, address, metro, phone)
    rent_page = RentPage(driver)
    rent_page.filling_order_date(date)
    text = rent_page.receive_text_view_status_button()
    text_button = 'Посмотреть статус'
    assert text_button == text

@allure.title('Тест перехода на главную после регистрации')
def test_if_click_logo_scooter_get_main_page(driver, personal_data, date):
    name = personal_data.get('name')
    last_name = personal_data.get('last_name')
    address = personal_data.get('address')
    metro = personal_data.get('metro')
    phone = personal_data.get('phone')
    base_page = BasePage(driver)
    base_page.click_cookie_button()
    base_page.click_order_button_in_header()
    scooter_page = WhoIsTheScooterFor(driver)
    scooter_page.filling_in_personal_data(name, last_name, address, metro, phone)
    rent_page = RentPage(driver)
    rent_page.filling_order_date(date)
    rent_page.click_on_view_status_button()
    base_page.click_logo_scotter()
    url = base_page.get_url()
    url_main = 'https://qa-scooter.praktikum-services.ru/'
    assert url_main == url

@allure.title('Тест перехода на главную яндекс')
def test_if_click_logo_yandex_get_main_ya(driver):
    base_page = BasePage(driver)
    base_page.click_logo_yandex()
    base_page.switch_new_tab()
    base_page.wait_new_tab()
    url_ya = base_page.get_url()
    url = 'https://dzen.ru/?yredirect=true'
    assert url_ya == url

