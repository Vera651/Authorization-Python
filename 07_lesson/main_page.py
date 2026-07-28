from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        self.driver.find_element(By.XPATH, f"//button[text()='Add to cart' and @data-test='{product_name}']").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        