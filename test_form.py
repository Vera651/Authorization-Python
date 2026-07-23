from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_interaction():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # Заполните поле "custname" значением "Иван Иванов"
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Иван Иванов")

    # Найдите кнопку отправки и кликните на нее
    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()

    driver.quit()