import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/selenium/6/6.html')

    # Используем метод .find_element() для поиска элементов математического уравнения
    first_part = browser.find_element(By.XPATH, '//span[@class = "num"][1]').text
    second_part = browser.find_element(By.XPATH, '//span[@class = "num"][2]').text
    third_part = browser.find_element(By.XPATH, '//span[@class = "num"][3]').text
    fourth_part = browser.find_element(By.XPATH, '//span[@class = "num"][4]').text

    # Составляем математическое уравнение и считаем его значение
    result = str((int(first_part[2:]) * int(second_part[:-1]) * int(third_part[:-1])) + int(fourth_part))
    # print(type(result))

    # Используем метод .find_elements() для поиска значений всех элементов выпадающего списка на странице при помощи XPath
    dropdown = browser.find_elements(By.TAG_NAME, 'option')

    # Проходимся по списку значений выпадающего списка, проверяем значение какого элемента равно result и записываем его в переменную
    number = (drop.text for drop in dropdown if drop.text == result)

    # Устанавливаем значение в выпадающем списке
    browser.find_element(By.XPATH,'//select[@id="selectId"]').send_keys(number)
    browser.find_element(By.XPATH,'//select[@id="selectId"]').click()

    # Нажимаем кнопку "Отправить"
    send = browser.find_element(By.XPATH, '//input[@id="sendbutton"]').click()

    # Записываем в переменную number, появившееся на странице число и выводим его
    number = browser.find_element(By.XPATH, '//p[@id="result"]').text
    print(number)

    time.sleep(3)


