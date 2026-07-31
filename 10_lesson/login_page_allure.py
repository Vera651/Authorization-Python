from selenium.webdriver.common.by import By


class LoginPage:
    """
    Страница авторизации SauceDemo.
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

    def login(self, username: str, password: str) -> None:
        """
        Авторизация пользователя.
        Args:
            username (str): Логин пользователя.
            password (str): Пароль пользователя.
        Returns:
            None
        """

        self.driver.find_element(
            By.ID,
            "user-name"
        ).send_keys(username)

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys(password)

        self.driver.find_element(
            By.ID,
            "login-button"
        ).click()