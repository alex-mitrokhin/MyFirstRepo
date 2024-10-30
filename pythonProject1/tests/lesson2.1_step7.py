from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной "x" через атрибут "valuex" у картинки сундука
    x_element = browser.find_element(By.ID,"treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    assert x == "519"
    # Вычислить математическую функцию от х
    y = calc(x)

    # Ввести ответ в текстовое поле
    text_field = browser.find_element(By.CSS_SELECTOR,"input[id='answer']")
    text_field.send_keys(y)

    # Отметить checkbox: "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR,"#robotsRule")
    radiobutton.click()

    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR,"button")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()