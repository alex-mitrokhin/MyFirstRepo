import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')

    fields = browser.find_elements(By.XPATH,'//input [@type="text"]')

    for field in fields:
        field.clear()

    verify = browser.find_element(By.XPATH, '//button[@id="checkButton"]').click()

    print(browser.switch_to.alert.text)


    time.sleep(2)