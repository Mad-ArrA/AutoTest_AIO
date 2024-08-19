from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time

# By.ID – Поиск элемента по уникальному идентификатору (id).
# Этот метод очень быстрый и надежный, но требует, чтобы у элемента был атрибут id.
element = driver.find_element(By.ID, "some_id")

# By.CSS_SELECTOR – Поиск элемента или элементов, используя селекторы CSS.
# Это гибкий и мощный метод, который может выразить сложные критерии поиска.
elements = driver.find_elements(By.CSS_SELECTOR, ".some_class")

# By.XPATH – Поиск элемента с помощью языка XPath.
# XPath позволяет создать более сложные запросы, но он менее читаемый и, возможно, будет работать медленнее, чем другие методы.
element = driver.find_element(By.XPATH, "//div[@attribute='value']")

# By.NAME – Поиск элемента по атрибуту name.
# Этот метод хорошо подходит для форм.
element = driver.find_element(By.NAME, "username")

# By.TAG_NAME – Поиск элемента по названию HTML-тега.
# Этот метод полезен, если нужно выбрать, например, все изображения на странице.
images = driver.find_elements(By.TAG_NAME, "img")

# By.CLASS_NAME – Поиск элемента или элементов по классу.
# Этот метод полезен, если у элементов есть общий класс.
buttons = driver.find_elements(By.CLASS_NAME, "btn")

# By.LINK_TEXT – Поиск элемента по точному тексту ссылки. Очень удобно, если текст уникален.
element = driver.find_element(By.LINK_TEXT, "Continue")

# By.PARTIAL_LINK_TEXT – Поиск элемента по частичному тексту ссылки.
# Удобно, когда точный текст ссылки неизвестен или динамичен.
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Cont")

# .find_element()
# Метод find_element() используется, когда вам нужно найти один конкретный элемент на странице. Он возвращает первый элемент,
# который соответствует заданным критериям поиска. Если элемент не найден, Selenium сгенерирует исключение NoSuchElementException.
# Ищем элемент с тегом img
elements = driver.find_elements(By.TAG_NAME, 'img')

# .find_elements()
# Метод find_elements() полезен, когда вы хотите получить список всех элементов, которые соответствуют заданным критериям.
# В отличие от find_element(), этот метод вернёт пустой список, если ничего не найдено, вместо того чтобы генерировать исключение.
# Ищем все элементы с классом some_class
elements = driver.find_elements(By.CLASS_NAME, 'some_class')

# Объект WebElement — ваш ключ к манипуляциям с элементом на странице.
# Вы можете применять к нему различные методы, такие как:
# .click() для симуляции клика мышью.
browser.find_element(By.ID, "some_button_id").click()

# .send_keys() для ввода текста (полезно для текстовых полей).
browser.find_element(By.NAME, "some_textbox_name").send_keys("Hello, World!")

# .get_attribute('some_attribute') для получения атрибутов, например, href у ссылок.
browser.find_element(By.TAG_NAME, "a").get_attribute("href")

# .text для получения видимого текста элемента.
browser.find_element(By.CLASS_NAME, "some_class_name").text

###########################################################################
# Сценарий 1: Каскадный поиск
# Иногда, чтобы добраться до конкретного элемента, нужно сначала найти его "родительский" элемент, и уже внутри него искать дочерний.
# Ищем родительский элемент
parent_element = driver.find_element(By.ID, 'parent_id')
# Ищем дочерний элемент внутри родительского
child_element = parent_element.find_element(By.CLASS_NAME, 'child_class')

# Или тот же самый поиск в одну строку
element = driver.find_element(By.ID, 'parent_id').find_element(By.CLASS_NAME, 'child_class')

###########################################################################
# Сценарий 2: Поиск внутри списка элементов
# Представьте, что у вас на странице несколько однотипных блоков, и в каждом из них есть кнопка или какой-то другой элемент,
# с которым нужно взаимодействовать.
# Ищем все блоки
blocks = driver.find_elements(By.CLASS_NAME, 'block')

# Проходим по каждому блоку и кликаем на кнопку внутри
for block in blocks:
    button = block.find_element(By.CLASS_NAME, 'button')
    button.click()

###########################################################################
# Сценарий 3: Проверка существования элементов
# Вы можете сначала проверить, есть ли на странице интересующие вас элементы, и только затем с ними взаимодействовать.
# Ищем все элементы с классом 'some_class'
elements = driver.find_elements(By.CLASS_NAME, 'some_class')

# Если элементы найдены, кликаем на первый
if elements:
    elements[0].click()

###########################################################################
# Пример кода:
# Псевдокод который делает запрос к несуществующему сайту,
# но наглядно демонстрирующий использование элементов find_element() и find_elements().

from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера в блоке with для автоматического закрытия
with webdriver.Chrome() as driver:
    # Открытие веб-страницы
    driver.get("http://some-news-website.com")

    # Ищем все блоки новостей
    news_blocks = driver.find_elements(By.CLASS_NAME, 'news-block')

    # Проходимся по каждому блоку
    for block in news_blocks:
        # В каждом блоке ищем заголовок
        title_element = block.find_element(By.CLASS_NAME, 'title')

        # Допустим, выводим текст каждого заголовка
        print("Заголовок новости:", title_element.text)

# Браузер закроется автоматически после выхода из блока with

# Сначала мы используем find_elements() для поиска всех элементов с классом .news-block.
# Полученный список сохраняем в переменную news_blocks.
#
# Затем мы проходимся по этому списку в цикле for.
#
# Внутри каждого блока news-block мы используем find_element() для поиска элемента с классом .title.
#
# Извлекаем и выводим текст из каждого найденного заголовка.
1. WebDriverWait(browser, 10)
# WebDriverWait — это класс из библиотеки Selenium, который используется для реализации явных ожиданий.
# В данном случае, мы создаем объект WebDriverWait, передавая ему два аргумента:
    browser: # это экземпляр драйвера браузера, с которым мы работаем (в нашем случае, это Chrome).
    10: # это максимальное количество времени (в секундах), в течение которого WebDriverWait будет пытаться выполнить условие,
        # указанное в методе until.
2. .until(...) #— Этот метод указывает, какое условие мы ожидаем выполнить.
                # Он будет опрашивать условие каждые несколько миллисекунд
                # до тех пор, пока условие не выполнится или пока не истечет максимальное время ожидания (в данном случае 10 секунд).
3. EC.element_to_be_clickable((By.ID, "btn")):
EC (или expected_conditions) # — это модуль в Selenium, который содержит набор предустановленных условий,
                            # которые можно использовать с WebDriverWait(далее подробно про EC).
element_to_be_clickable() # — это одно из этих условий. Оно проверяет, что элемент не только присутствует на странице,
                            # но и видим, а также активен, так что по нему можно кликнуть (далее подробно про все функции).
(By.ID, "btn") # — это способ указать, какой именно элемент мы ищем.
                # В данном случае, мы ищем элемент по его идентификатору (ID), который равен "btn".

WebDriverWait(browser, poll_frequency=0.5, timeout=10).until(EC.element_to_be_clickable((By.ID, "btn")))
# Параметры WebDriverWait:
    browser: #Экземпляр WebDriver (например, Ie, Firefox, Chrome или Remote)

    poll_frequency=float: #(необязательный): Интервал ожидания между попытками. По умолчанию равен значению 0.5.

    timeout=float: #Количество секунд до таймаута

    .until(method): #Ожидает, пока предоставленный method вернет что-либо, кроме False.
    # Если method продолжает возвращать False до истечения времени ожидания, будет вызвано исключение TimeoutException.

    .until_not(method): #Ожидает, пока предоставленный method не вернет False.
    # Если метод не вернет False до истечения времени ожидания, будет вызвано исключение TimeoutException.

#Как  работаетuntil() и until_not()?

# Когда вы вызываете метод until(method), Selenium регулярно (с интервалом, заданным параметром poll_frequency=0.5) проверяет,
# выполняется ли указанное вами условие.

