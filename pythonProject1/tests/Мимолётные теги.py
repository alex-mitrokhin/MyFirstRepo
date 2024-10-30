import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/expectations/6/index.html')

    button = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,'btn'))).click()

    element = WebDriverWait(browser,25).until(EC.presence_of_element_located((By.CLASS_NAME,'BMH21YY')))

    print(element.text)

    time.sleep(2)