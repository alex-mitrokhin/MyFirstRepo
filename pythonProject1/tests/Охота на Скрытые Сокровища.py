import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/methods/1/index.html')

    code = browser.find_element(By.ID,'result').text

    while code == 'refresh page':
        browser.refresh()
        code = browser.find_element(By.ID,'result').text
        if code != 'refresh page':
            print(code)

    time.sleep(2)


