from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на вращающуюся кнопку Button
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Считать значение для переменной "x" через атрибут "text"
    x = browser.find_element(By.ID, "input_value").text

    # Вычислить математическую функцию от х
    y = calc(x)

    # Ввести ответ в текстовое поле
    text_field = browser.find_element(By.NAME, "text").send_keys(y)

    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, "button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()