from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def sort_geozon():
    driver = webdriver.Chrome()
    driver.get("http://192.168.111.16/litecart/admin/?app=geo_zones&doc=geo_zones")
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()


    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "username").send_keys("admin")

    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("admin")

    driver.find_element(By.NAME, "login").click()

    wait = WebDriverWait(driver, 10)

    countries = []
    countries_name = driver.find_elements(By.CSS_SELECTOR, "tr.row")
    for name in countries_name:
        countries.append(name.find_element(By.CSS_SELECTOR, "td:nth-child(3) a").get_attribute("href"))
        print(countries)

    for c in countries:
        driver.get(c)

        zones = []
        rows = driver.find_elements(By.CSS_SELECTOR, "table#table-zones td:nth-child(3) select")
        for row in rows:
            zones.append(row.find_element(By.CSS_SELECTOR, "[selected = selected]").get_attribute("innerText"))
            print(zones)

        assert sorted(zones) == zones, "Не отсортирован"

    driver.quit()

sort_geozon()