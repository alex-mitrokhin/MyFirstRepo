from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    fragments = browser.find_elements(By.XPATH, '//div[@class="text"]/p[2]')

    summ = 0

    numbers = sum(int(p.text) for p in fragments)
    print(numbers)