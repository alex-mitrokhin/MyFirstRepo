import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(3)

    input = browser.find_element(By.ID,"ember457").click()

    first_name = browser.find_element(By.ID, "id_login_email")
    first_name.send_keys("alex.mitrohin2016@yandex.ru")

    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("E4P1Vq6n")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".sign-form")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
