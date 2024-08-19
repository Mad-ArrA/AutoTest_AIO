from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import time
import allure
import subprocess

# def run_tests():
#     # Запуск pytest с указанием директории для Allure отчетов
#     subprocess.run(["pytest", "--alluredir=allure-results"])
#
# def generate_report():
#     # Запуск генерации Allure отчета
#     subprocess.run(["allure", "serve", "allure-results"])

@pytest.fixture
def driver():
    with allure.step("Инициализация драйвера браузера"):
        driver = webdriver.Chrome()  # Убедитесь, что chromedriver находится в PATH
    yield driver
    driver.quit()
    # run_tests()
    # generate_report()

@allure.feature('Connect Wallet')
@allure.story('MetaMask Wallet Connection')
def test_open_page(driver):
    with allure.step("Открытие страницы и клик на Connect Wallet"):
        driver.get("https://aio-pro-frontend.vercel.app/connect")

        connect_wallet_button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "connect-wallet__open"))
        )
        connect_wallet_button.click()

    with allure.step("Выбор MetaMask для подключения"):
        button_connect = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "connectors__connect"))
        )

        if button_connect:
            button_connect[1].click()

    time.sleep(30)

    with allure.step("Ввод пароля и авторизация"):
        password_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "field__input"))
        )
        password_input.send_keys("Arm121309!")

        button_login = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "actions__submit"))
        )
        button_login.click()

    with allure.step("Проверка успешной авторизации"):
        assert WebDriverWait(driver, 10).until(
            ec.url_to_be("https://aio-pro-frontend.vercel.app/accounts/evm/wallets")
        )

    time.sleep(10)



    # driver.save_screenshot("screenshot.png")


# def test_element_presence(driver):
#     driver.get("https://example.com")
#     elem = driver.find_element(By.TAG_NAME, "h1")
#     assert elem.text == "Example Domain"
#
#
# def test_google_search(driver):
#     driver.get('https://www.google.com')
#     search_box = driver.find_element(By.NAME, 'q')
#     search_box.send_keys('pytest')
#     search_box.submit()
#     assert 'pytest' in driver.title
#     driver.save_screenshot("page.html")
