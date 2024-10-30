import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/selenium/1/1.html')

    # Используем метод .find_elements() для поиска всех возможных полей ввода на странице при помощи XPath
    input_forms = browser.find_elements(By.XPATH, '//div[@class="form_box"]/input')

    # Создаем список значений для последующего заполнения полей
    texts = ['Алексей', 'Митрохин', 'Владимирович', 36, 'Пенза', 'aleksey.mitrokhin@osinit.com']

    # Проходимся по списку значений и заполняем поля ввода
    for i, input_form in enumerate(input_forms):
        input = input_form.send_keys(texts[i])

    # Находим кнопку "Отправить" и нажимаем на нее
    button = browser.find_element(By.XPATH,'//input[@type="button"]').click()

    time.sleep(5)
