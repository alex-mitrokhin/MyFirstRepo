from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    fragments = browser.find_elements(By.XPATH, '//div[@class="text"]/p')

    summ = 0

    for p in fragments:
        number = int(p.text)

        summ += number

    print(int(summ))
