from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

# Найдите поле ввода с названием custname.
    name_field = driver.find_element(By.NAME, "custname")
    
# Введите в него ваше имя.
    name_field.send_keys("Вера Крючкова")

# Найдите кнопку Submit и нажмите на нее.
    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_btn.click()

# Проверьте, что после нажатия URL изменился.
    assert "https://httpbin.org/post" in driver.current_url

    driver.quit()
    