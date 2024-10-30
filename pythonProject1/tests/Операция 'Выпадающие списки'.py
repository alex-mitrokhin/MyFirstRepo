import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/selenium/7/7.html')

    # Используем метод .find_elements() для поиска значений всех элементов выпадающего списка на странице при помощи XPath
    dropdowns = browser.find_elements(By.TAG_NAME, 'option')

    # Проходимся по списку элементов выпадающего списка и суммируем их
    numbers = sum(int(dropdown.text) for dropdown in dropdowns)
    print(numbers)

    # Устанавливаем получившийся результат в поле ввода на сайте и нажимаем кнопку "Отправить"
    input_field = browser.find_element(By.XPATH,'//input[@type="text"]').send_keys(numbers)
    send = browser.find_element(By.XPATH, '//input[@id="sendbutton"]').click()

    # Записываем в переменную number, появившееся на странице число и выводим его
    number = browser.find_element(By.XPATH, '//p[@id="result"]').text
    print(number)

    time.sleep(3)