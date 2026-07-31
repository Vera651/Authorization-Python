from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage


def test_1 ():
    browser = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator_page = CalculatorPage(browser)

    calculator_page.set_delay("45")

    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    result_text = calculator_page.get_result()
    assert result_text == "15", f"Результат неверный: {result_text}"

    browser.quit()