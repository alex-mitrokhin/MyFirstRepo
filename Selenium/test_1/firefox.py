from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://vk.com/")
page_title = driver.title
print("Заголовок страницы: " + str(page_title))

driver.get("https://ya.ru/")
page_title_1 = driver.title
print("Заголовок страницы: " + str(page_title_1))
driver.back()
assert driver.title == page_title, "Мы не вернулись обратно"

driver.refresh()
URL_page = driver.current_url
print(URL_page)

driver.forward()
assert driver.title == page_title_1, "Мы не вернулись обратно"

