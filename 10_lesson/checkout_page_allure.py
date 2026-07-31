from selenium.webdriver.common.by import By


class CheckoutPage:
    """
    Страница оформления заказа SauceDemo.
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

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """
        Заполнение формы оформления заказа.
        Args:
            first_name (str): Имя покупателя.
            last_name (str): Фамилия покупателя.
            postal_code (str): Почтовый индекс.
        Returns:
            None
        """

        self.driver.find_element(
            By.ID,
            "first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.ID,
            "last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys(postal_code)

        self.driver.find_element(
            By.ID,
            "continue"
        ).click()

    def verify_total(self, expected_total: str) -> None:
        """
        Проверка итоговой суммы заказа.
        Args:
            expected_total (str): Ожидаемая сумма заказа.
        Returns:
            None
        """

        total_element = self.driver.find_element(
            By.CLASS_NAME,
            "summary_total_label"
        )

        actual_total = total_element.text.split("$")[-1]

        assert actual_total == expected_total, (
            f"Ожидалась сумма {expected_total}, "
            f"получена {actual_total}"
        )