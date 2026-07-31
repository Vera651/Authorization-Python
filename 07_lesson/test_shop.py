from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    main_page.add_to_cart("sauce-labs-backpack")
    main_page.add_to_cart("sauce-labs-bolt-t-shirt")
    main_page.add_to_cart("sauce-labs-onesie")
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Вера", "Крючкова", "000350")
    checkout_page.verify_total("58.29")

    driver.quit()