from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(
ChromeDriverManager().install()))

browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

input_field = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.ID, "delay")))

input_field.clear() 
input_field.send_keys("45") 

button_7 = browser.find_element(By.XPATH, "//span[text()='7']").click()
button_plus = browser.find_element(By.XPATH, "//span[text()='+']").click()
button_8 = browser.find_element(By.XPATH, "//span[text()='8']").click()
button_equals = browser.find_element(By.XPATH, "//span[text()='=']").click()

result = WebDriverWait(browser, 50).until(
     EC.visibility_of_element_located((By.CLASS_NAME, "screen"))
)
result_text = result.text

assert result_text == "15", f"Результат неверный: {result_text}"

browser.quit()
