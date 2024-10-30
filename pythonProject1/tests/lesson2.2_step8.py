from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan_petrov@mail.ru")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname("c:/Users/aleksey.mitrokhin/Project_ОТ-ОЙЛ/")) # получаем путь к директории файла
    print(current_dir)
    file_path = os.path.join(current_dir, 'request.txt')  # добавляем к этому пути имя файла

    element = browser.find_element(By.ID,"file")
    element.send_keys(file_path)

    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, "button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()