import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('c:/Users/aleksey.mitrokhin/MyFirstRepo/pythonProject1/coordinates.crx')

# Инициализируем драйвер Chrome
with webdriver.Chrome(options=options_chrome) as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()

    sum_cookies = 0

    for cookie in cookies:
        if int(cookie['name'].split('_')[2]) % 2 == 0:
            sum_cookies += int(cookie['value'])
    print(sum_cookies)
