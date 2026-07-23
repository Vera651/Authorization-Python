from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")

# Найдите и кликните на ссылку HTML Form.
    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()

# Проверьте, что URL изменился на /forms/post.
    assert "/forms/post" in driver.current_url

# Вернитесь назад на главную страницу.
    driver.back()

# Проверьте, что вернулись на исходный URL.
    assert "https://httpbin.org/" == driver.current_url
    
    driver.quit()
