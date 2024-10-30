from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('c:/Users/aleksey.mitrokhin/MyFirstRepo/pythonProject1/coordinates.crx')

# Инициализируем драйвер Chrome
with webdriver.Chrome(options=options_chrome) as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/scroll/4/index.html')

    # Используем метод .find_elements() для поиска всех ссылок на странице при помощи XPath
    elements = browser.find_elements(By.XPATH, '//button[@class="btn"]')

    result_sum = 0

    for element in elements:
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)

        element.click()

        result_sum += int(browser.find_element(By.XPATH,'//p[@id="result"]').text)

    print(result_sum)