from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/selenium/4/4.html')

    # Используем метод .find_elements() для поиска всех чек-боксов на странице при помощи XPath
    check_boxes = browser.find_elements(By.XPATH, '//input[@class="check"]')

    # Проходимся по списку найденных чек-боксов и активируем их
    for check in check_boxes:
        check.click()

    # Находим кнопку "Отправить" и нажимаем на нее
    send = browser.find_element(By.XPATH, '//input[@class="btn"]').click()

    # Находим итоговое число на странице, записываем в переменную и выводим
    number = browser.find_element(By.XPATH, '//p[@id="result"]').text
    print(number)
