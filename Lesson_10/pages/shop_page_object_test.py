import allure
from selenium import webdriver
from Lesson_10.pages.ShopPage import ShopPage

@allure.epic("Allure тесты")
@allure.title("Заказ товаров в интернет-магазине")
@allure.feature("Интернет-магазин")
@allure.description("Заказ товара на сумму $58.29")
@allure.severity("Critical")
def test_total_sum():
    with allure.step("Открытие страницы и авторизация на сайте"):
      driver = webdriver.Chrome()
      shop_page = ShopPage(driver)
      shop_page.open_authorization()
    # страница 1
      shop_page.input_login("standard_user")
      shop_page.input_password("secret_sauce")

    with allure.step("Нажатие на кнопку 'login'"):
      shop_page.click_login_button()

    with allure.step("Добавление товара и переход в корзину"):
    #страница 2
      shop_page.add_items_to_cart()
      shop_page.go_in_cart()

    with allure.step("Нажатие на кнопку 'checkout'"):
      shop_page.click_checkout_button()

    with allure.step("Заполнение формы своими данными"):
    #страница 3
      shop_page.input_first_name("Anastasiia")
      shop_page.input_last_name("Gosteeva")
      shop_page.input_postal_code("432064")

    with allure.step("Нажатие на кнопку 'continue'"):
      shop_page.click_continue_button()

    with allure.step("Получение и проверка результата"):
    #страница 4
      shop_page.get_total_sum()
      result = shop_page.result()
      assert result == "Total: $58.29"


    driver.quit()