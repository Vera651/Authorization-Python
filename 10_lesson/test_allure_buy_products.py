import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from login_page_allure import LoginPage
from main_page_allure import MainPage
from cart_page_allure import CartPage
from checkout_page_allure import CheckoutPage


@allure.title("Покупка товаров в SauceDemo")
@allure.description(
    "Тест проверяет авторизацию пользователя, "
    "добавление товаров в корзину и оформление заказа"
)
@allure.feature("Интернет-магазин SauceDemo")
@allure.severity(allure.severity_level.CRITICAL)
def test_buy_products():
    """
    Проверка полного сценария покупки товаров.
    Returns:
        None
    """

    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

    try:
        with allure.step("Открыть страницу авторизации"):
            driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)

        with allure.step("Авторизоваться под стандартным пользователем"):
            login_page.login(
                "standard_user",
                "secret_sauce"
            )

        main_page = MainPage(driver)

        with allure.step("Добавить товары в корзину"):
            main_page.add_to_cart("sauce-labs-backpack")
            main_page.add_to_cart("sauce-labs-bolt-t-shirt")
            main_page.add_to_cart("sauce-labs-onesie")

        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()

        cart_page = CartPage(driver)

        with allure.step("Проверить товары в корзине"):
            cart_page.verify_cart_contents(
                [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bolt T-Shirt",
                    "Sauce Labs Onesie"
                ]
            )

        with allure.step("Перейти к оформлению заказа"):
            cart_page.checkout()

        checkout_page = CheckoutPage(driver)

        with allure.step("Заполнить данные покупателя"):
            checkout_page.fill_form(
                "Вера",
                "Крючкова",
                "000350"
            )

        with allure.step("Проверить итоговую сумму заказа"):
            checkout_page.verify_total("58.29")

    finally:
        driver.quit()