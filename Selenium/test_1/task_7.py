import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def checkSticker():
    driver = webdriver.Chrome()
    driver.get("http://192.168.111.16/litecart")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    product_list = driver.find_elements(By.CSS_SELECTOR, "ul.listing-wrapper >li")

    for element in product_list:
        stickers = element.find_elements(By.CSS_SELECTOR, "div.sticker")
        if len(stickers) == 1:
            print("One sticker!")
        else:
            print("No sticker!")

    time.sleep(2)

    driver.close()

checkSticker()