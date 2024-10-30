import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')

    fields = browser.find_elements(By.XPATH,'//input[@class="text-field"]')

    for field in fields:
        if not field.get_attribute("disabled"):
            field.clear()

    verify = browser.find_element(By.XPATH, '//button[@id="checkButton"]').click()

    print(browser.switch_to.alert.text)


    time.sleep(2)