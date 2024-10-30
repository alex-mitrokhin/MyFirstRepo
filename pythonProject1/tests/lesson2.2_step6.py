from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной "x"
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычислить математическую функцию от х
    y = calc(x)

    # Ввести ответ в текстовое поле
    text_field = browser.find_element(By.ID, "answer").send_keys(y)

    # Проскроллить страницу вниз
    submit = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

    # Отметить checkbox: "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, "button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()