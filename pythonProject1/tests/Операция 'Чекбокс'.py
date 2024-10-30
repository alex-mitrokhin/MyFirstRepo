import time

from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('c:/Users/aleksey.mitrokhin/MyFirstRepo/pythonProject1/coordinates.crx')

# Инициализируем драйвер Chrome
with webdriver.Chrome(options=options_chrome) as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')

    checks = browser.find_elements(By.XPATH, '//div[@class="parent"]')

    result_sum = 0

    for check in checks:
        if check.find_element(By.XPATH, '//input[@class="checkbox"]').is_selected():
            result_sum += int(check.find_element(By.TAG_NAME, 'textarea').text)
    print(result_sum)