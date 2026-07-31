from selenium.webdriver.common.by import By


class CalculatorPage:
    """
    Страница калькулятора.
    """

    def __init__(self, driver):
        """
        Инициализация страницы.
        Args:
            driver (WebDriver): Экземпляр браузера Selenium.
        Returns:
            None
        """

        self.driver = driver

    def set_delay(self, delay_time: str) -> None:
        """
        Установка задержки вычисления.
        Args:
            delay_time (str): Время задержки в секундах.
        Returns:
            None
        """

        delay_field = self.driver.find_element(
            By.ID,
            "delay"
        )

        delay_field.clear()
        delay_field.send_keys(delay_time)

    def click_button(self, button_value: str) -> None:
        """
        Нажатие кнопки калькулятора.
        Args:
            button_value (str): Значение кнопки.
        Returns:
            None
        """

        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{button_value}']"
        )

        button.click()

    def get_result(self) -> str:
        """
        Получение результата вычисления.
        Returns:
            str: Значение на экране калькулятора.
        """

        result_field = self.driver.find_element(
            By.CSS_SELECTOR,
            ".screen"
        )

        return result_field.text