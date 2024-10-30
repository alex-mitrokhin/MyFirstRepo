from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('c:/Users/aleksey.mitrokhin/MyFirstRepo/pythonProject1/coordinates.crx')

# Инициализируем драйвер Chrome
with webdriver.Chrome(options=options_chrome) as browser:
    # Открываем веб-страницу по заданному URL
    browser.get('https://parsinger.ru/methods/5/index.html')

    # Используем метод .find_elements() для поиска всех ссылок на странице при помощи XPath
    links = browser.find_elements(By.XPATH, '//a')

    # Создаем пустой список для ссылок
    hrefs = []

    # Проходимся по списку найденных ссылок и добавляем ссылки в созданный ранее список hrefs
    for link in links:
        hrefs.append(link.get_attribute('href'))

    # Создаем переменные: срок жизни cookie веб-страницы и итоговый результат для cookie с самым долгим сроком жизни
    expiry = 0
    result = 0

    # Проходимся по списку ссылок hrefs, открываем каждую из них и сохраняем в переменную cookies список всех cookies
    for href in hrefs:
        browser.get(href)
        cookies = browser.get_cookies()

    # Проходимся по списку cookies, анализируем срок жизни cookie['expiry'] каждой веб-страницы
        for cookie in cookies:
            print(cookie['expiry'])

    # Выполняем проверку: если значение cookie['expiry'] очередной веб-страницы больше значения переменной expiry, то записываем значение в переменную
            if cookie['expiry'] > expiry:
                expiry = cookie['expiry']

    # На веб-странице с cookie['expiry'] с самым долгим сроком жизни извлекаем число из тега <p id="result">INT</p>
                result = browser.find_element(By.XPATH,'//p[@id="result"]').text

    print(result)




