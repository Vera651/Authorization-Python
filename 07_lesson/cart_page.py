from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()

    def verify_cart_contents(self, expected_items):
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        actual_items = [item.text for item in cart_items]