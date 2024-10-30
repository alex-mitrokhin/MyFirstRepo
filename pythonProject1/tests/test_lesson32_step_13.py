from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")

    first_name.send_keys("Petr")
    last_name.send_keys("Ivanov")
    email.send_keys("qwer@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert welcome_text == "Congratulations! You have successfully registered!"

def test_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")

    first_name.send_keys("Petr")
    last_name.send_keys("Ivanov")
    email.send_keys("qwer@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert welcome_text == "Congratulations! You have successfully registered!"


if __name__ == "__main__":
    pytest.main()