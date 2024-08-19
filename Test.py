from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()  # Убедись, что chromedriver находится в PATH
    yield driver
    driver.quit()


def test_open_page(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    time.sleep(10)
    driver.save_screenshot("screenshot.png")


def test_element_presence(driver):
    driver.get("https://example.com")
    elem = driver.find_element(By.TAG_NAME, "h1")
    assert elem.text == "Example Domain"


def test_google_search(driver):
    driver.get('https://www.google.com')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('pytest')
    search_box.submit()
    assert 'pytest' in driver.title
    driver.save_screenshot("page.html")
