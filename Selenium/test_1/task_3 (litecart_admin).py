from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

def task_3():

    driver = webdriver.Chrome()
    driver.get("http://192.168.111.16/litecart/admin")
    driver.maximize_window()
    time.sleep(2)

    Username = driver.find_element(By.NAME,"username").send_keys("alexey")
    time.sleep(1)

    Password = driver.find_element(By.NAME, "password").send_keys("password")
    time.sleep(1)

    Remember_Me = driver.find_element(By.NAME, "remember_me").click()
    time.sleep(1)

    Login = driver.find_element(By.NAME,"login").click()
    time.sleep(1)
    driver.quit()

task_3()