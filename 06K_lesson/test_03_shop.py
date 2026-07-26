from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
driver.find_element(By.ID, "checkout").click() #кнопка не нажимается

driver.find_element(By.ID, "first-name").send_keys("Вера")
driver.find_element(By.ID, "last-name").send_keys("Крючкова")
driver.find_element(By.ID, "postal-code").send_keys("000350")
driver.find_element(By.ID, "continue").click()

total_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
)
total = total_element.text

assert total.endswith("$58.29")

print("OK")

driver.quit()
