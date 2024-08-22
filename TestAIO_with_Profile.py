from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pytest
import time
import allure

NAME_GROUP = "Test Group 2"
# Устанавливает область видимости фикстуры на модульный уровень.
# Это означает, что браузер будет инициализироваться один раз для всех тестов в модуле и будет закрываться после завершения всех тестов.
@pytest.fixture(scope="module")
def driver():
    with allure.step("Инициализация драйвера браузера"):
        options_chrome = webdriver.ChromeOptions()
        # Указываем путь к профилю пользователя
        options_chrome.add_argument('user-data-dir=C:\\Users\\ArrA\\AppData\\Local\\Google\\Chrome\\User Data')
        # Инициализируем драйвер с указанными опциями
        driver = webdriver.Chrome(options=options_chrome)
        # driver.set_window_size("1936x1048")
        driver.get("https://aio-pro-frontend.vercel.app/connect")
        yield driver
        driver.quit()

@allure.feature('Connect Wallet')
@allure.story('MetaMask/Rabby Wallet Connection')
# @pytest.mark.skip(reason="Тест временно отключен")
def test_click_login(driver):
    with allure.step("Открытие страницы и клик на Connect Wallet"):
        connect_wallet_button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "connect-wallet__open"))
        )
        connect_wallet_button.click()

    with allure.step("Выбор MetaMask для подключения"):
        button_connect = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "connectors__connect"))
        )

        if button_connect:
            button_connect[2].click()

    time.sleep(10)  # Даем время на открытие окна

    with allure.step("Ввод пароля и авторизация"):
        password_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "field__input"))
        )
        password_input.click()

    time.sleep(10)

    try:
        # Проверка, что кнопка видима и кликабельна
        button_login = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "actions__submit"))
        )

        # Дополнительно можно проверить, что кнопка не заблокирована (не имеет атрибута disabled)
        is_enabled = button_login.is_enabled()

        if is_enabled:
            button_login.click()
        else:
            print("Кнопка actions__submit недоступна для клика, пропускаем этот шаг.")

    except TimeoutException:
        print(
            "Кнопка actions__submit не была найдена на странице или не была кликабельной в течение ожидаемого времени, продолжаем выполнение.")

    with allure.step("Проверка успешной авторизации"):
        assert WebDriverWait(driver, 10).until(
            ec.url_to_be("https://aio-pro-frontend.vercel.app/accounts/evm/wallets")
        )

@allure.feature('Create Group')
@allure.story('Create group account manager')
def test_create_group_account_manager(driver):
    with allure.step("Добавление группы"):
        add_group_accmanager = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "add-wallet-group"))
        )
        add_group_accmanager.click()

    with allure.step("Ввод названия группы"):
        name_group_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "custom-input__input"))
        )
        name_group_input.send_keys(NAME_GROUP)

    with allure.step("Кнопка Create"):
        button_create_group = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "left-side__ok"))
        )
        button_create_group.click()

    time.sleep(10)

    with allure.step("Проверка успешного добавления группы"):
        assert WebDriverWait(driver, 10).until(
            ec.text_to_be_present_in_element((By.CLASS_NAME, "group-wallets"),NAME_GROUP)
        )