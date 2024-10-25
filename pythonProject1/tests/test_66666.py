import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

uncorrected_results = []

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(55)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(''.join(uncorrected_results))

@pytest.mark.parametrize('code', ["236895", "236896"])

class TestMainPage1():

    def test_guest_should_see_login_link(self, browser, code):
        link = f"https://stepik.org/lesson/{code}/step/1"
        browser.get(link)

        input = WebDriverWait(browser, 55).until(EC.element_to_be_clickable((By.ID, "ember457"))).click()

        first_name = WebDriverWait(browser, 55).until(EC.visibility_of_element_located((By.ID, "id_login_email")))
        first_name.send_keys("alex.mitrohin2016@yandex.ru")

        password = WebDriverWait(browser, 55).until(EC.visibility_of_element_located((By.ID, "id_login_password")))
        password.send_keys("E4P1Vq6n")

        # Отправляем заполненную форму
        button = WebDriverWait(browser, 55).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-form"))).click()


        textarea = WebDriverWait(browser, 55).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))
        answer = str(math.log(int(time.time())))
        print(answer)
        textarea.send_keys(answer)

        submit_button = WebDriverWait(browser, 55).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        browser.execute_script("arguments[0].click();", submit_button)
        time.sleep(2)
        # Ответ в черном поле и запись в переменную
        result_element = WebDriverWait(browser, 55).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        result_text = result_element.text

        if result_text != "Correct!":
            uncorrected_results.append(result_text)

        assert result_text == "Correct!", f"Error {result_text}"

