from selenium.webdriver.common.by import By


class MainPage:
    """
    Главная страница магазина SauceDemo с товарами.
    """

    def __init__(self, driver):
        """
        Инициализация страницы.
        Args:
            driver (WebDriver): Экземпляр браузера Selenium
        Returns:
            None
        """

        self.driver = driver

    def add_to_cart(self, product_name: str) -> None:
        """
        Добавление товара в корзину.
        Args:
            product_name (str): Название товара.
        Returns:
            None
        """

        self.driver.find_element(
            By.XPATH,
            f"//button[text()='Add to cart' and "
            f"@data-test='add-to-cart-{product_name}']"
        ).click()

    def go_to_cart(self) -> None:
        """
        Переход в корзину.
        Returns:
            None
        """

        self.driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()