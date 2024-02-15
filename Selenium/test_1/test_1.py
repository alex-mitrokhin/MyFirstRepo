from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.ru")

element_1 = driver.find_element("name", "q")
element_1.click()
element_1.clear()

element_1.send_keys(Keys.ENTER, "Python")
element_2 = driver.find_element("name", "btnK")
element_2.click()
time.sleep(2)
