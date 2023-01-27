from selenium import webdriver
from selenium.webdriver.common.by import By
# Выбираем драйвер для браузера Chrome
driver = webdriver.Chrome()
driver.get('https://penza.cian.ru/')

# Ищем элемент forBusiness на странице и кликаем по нему
#search = driver.find_element(By.ID,'geo-suggest-input').send_keys('')
#searchButton = driver.find_element(By.XPATH,'//*[@id="frontend-mainpage"]/section/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[3]/span/span[2]/a').click()
