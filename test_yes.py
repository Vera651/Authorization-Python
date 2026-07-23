from selenium import webdriver
from selenium.webdriver.common.by import By

def test_element_state():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")

# Найдите радио-кнопку "Yes" и проверьте:
    radio_btn = driver.find_element(By.ID, "yesRadio")

# 1. Что она отображается
    assert radio_btn.is_displayed() == True

# 2. Что она доступна для клика (через метку)
    label = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    assert label.is_enabled() == True

    driver.quit()