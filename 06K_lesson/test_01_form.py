from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Edge()

browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

browser.find_element(By.NAME, "first-name").send_keys("Иван")
browser.find_element(By.NAME, "last-name").send_keys("Петров")
browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
browser.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
browser.find_element(By.NAME, "phone").send_keys("+7985899998787")
# Поле Zip code оставить пустым
browser.find_element(By.NAME, "city").send_keys("Москва")
browser.find_element(By.NAME, "country").send_keys("Россия")
browser.find_element(By.NAME, "job-position").send_keys("QA")
browser.find_element(By.NAME, "company").send_keys("SkyPro")

submit_button = browser.find_element(By.CLASS_NAME, "btn-outline-primary")
submit_button.click()

print("Готово")

browser.quit()
