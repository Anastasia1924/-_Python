import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shop(driver):
    # Откройте страницу: https://www.saucedemo.com/
    driver.get("https://www.saucedemo.com/")
    #Авторизуйтесь как пользователь standard_user
    user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
    user_name.clear()
    user_name.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.clear()
    password.send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    #Добавьте в корзину товары
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    #Перейдите в корзину
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    #Нажмите Checkout
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    #Заполните форму своими данными
    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.clear()
    first_name.send_keys("Anastasiia")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.clear()
    last_name.send_keys("Gosteeva")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.clear()
    postal_code.send_keys("432064")
    #Нажмите кнопку Continue
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    #Прочитайте со страницы итоговую стоимость (Total)
    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    print(total)
    #Проверьте, что итоговая сумма равна $58.29
    result = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    assert result == "Total: $58.29"