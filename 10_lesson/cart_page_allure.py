from selenium.webdriver.common.by import By


class CartPage:
    """
    Страница корзины SauceDemo.
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

    def checkout(self) -> None:
        """
        Переход к оформлению заказа.
        Returns:
            None
        """

        self.driver.find_element(
            By.ID,
            "checkout"
        ).click()

    def verify_cart_contents(self, expected_items: list[str]) -> None:
        """
        Проверка наличия товаров в корзине.
        Args:
            expected_items (list[str]): Список ожидаемых товаров.
        Returns:
            None
        """

        cart_items = self.driver.find_elements(
            By.CLASS_NAME,
            "cart_item"
        )

        actual_items = [
            item.text
            for item in cart_items
        ]

        for item in expected_items:
            assert any(
                item in cart_item
                for cart_item in actual_items
            ), f"Товар {item} отсутствует в корзине"