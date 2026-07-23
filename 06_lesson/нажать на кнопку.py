from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()

element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Data loaded with AJAX get request.')]")))

print("Data loaded with AJAX get request.")

driver.quit()