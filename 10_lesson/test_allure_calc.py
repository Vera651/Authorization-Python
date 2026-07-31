import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage


@allure.title("Проверка сложения в калькуляторе")
@allure.description(
    "Тест проверяет выполнение операции сложения "
    "двух чисел в калькуляторе с задержкой вычисления"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_sum():
    """
    Проверка сложения чисел в калькуляторе.

    Returns:
        None
    """

    browser = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )

    try:
        with allure.step("Открыть страницу калькулятора"):
            browser.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

        calculator_page = CalculatorPage(browser)

        with allure.step("Установить задержку вычисления 45 секунд"):
            calculator_page.set_delay("45")

        with allure.step("Нажать кнопку 7"):
            calculator_page.click_button("7")

        with allure.step("Нажать кнопку сложения"):
            calculator_page.click_button("+")

        with allure.step("Нажать кнопку 8"):
            calculator_page.click_button("8")

        with allure.step("Нажать кнопку равно"):
            calculator_page.click_button("=")

        with allure.step("Ожидать появления результата 15"):
            wait = WebDriverWait(browser, 46)

            wait.until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, ".screen"),
                    "15"
                )
            )

        with allure.step("Проверить результат вычисления"):
            result_text = calculator_page.get_result()

            assert result_text == "15", (
                f"Ожидался результат 15, "
                f"получен {result_text}"
            )

    finally:
        browser.quit()