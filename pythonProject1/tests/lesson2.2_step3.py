from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Значение первой цифры
    first_number = browser.find_element(By.ID, "num1")
    first_value = first_number.text

    # Значение второй цифры
    last_number = browser.find_element(By.ID, "num2")
    last_value = last_number.text

    # Сумма цифр
    summa = int(first_value) + int(last_value)

    # Выбрать в выпадающем списке значение равное расчитанной сумме цифр
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summa))

    # Нажать кнопку "Submit"
    submit = browser.find_element(By.TAG_NAME,"button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()