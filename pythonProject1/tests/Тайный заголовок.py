import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/expectations/4/index.html')

    button = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,'btn'))).click()

    title = WebDriverWait(browser,25).until(EC.title_contains('JK8HQ'))

    print(browser.title)

    time.sleep(2)