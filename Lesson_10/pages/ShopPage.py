import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Интернет-магазин")
class ShopPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()


    @allure.step("Открытие страницы и ввод логина и пароля")
    def open_authorization(self):
        self._driver.get("https://www.saucedemo.com/")
        WebDriverWait(self._driver, 10, 0.1).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div")))
    #страница 1
    def input_login(self, login):
        input_username = self._driver.find_element(By.CSS_SELECTOR, "#user-name")
        input_username.clear()
        input_username.send_keys(login)

    def input_password(self, password ):
        input_password = self._driver.find_element(By.CSS_SELECTOR, "#password")
        input_password.clear()
        input_password.send_keys(password)


    @allure.step("Нажатие на кнопку 'login'")
    def click_login_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        WebDriverWait(self._driver, 10, 0.1).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".inventory_container")))


    @allure.step("Добавление товара и переход в корзину")
    #страница 2
    def add_items_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_in_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()


    @allure.step("Нажатие на кнопку 'checkout'")
    def click_checkout_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        WebDriverWait(self._driver, 10, 0.1).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".checkout_info_container")))


    @allure.step("Ввод имени, фамилии и индекса")
    #страница 3
    def input_first_name(self, first_name):
        input_first_name = self._driver.find_element(By.CSS_SELECTOR, "#first-name")
        input_first_name.clear()
        input_first_name.send_keys("Anastasiia")

    def input_last_name(self, last_name):
        input_last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name")
        input_last_name.clear()
        input_last_name.send_keys("Gosteeva")

    def input_postal_code(self, postal_code):
        input_postal_code = self._driver.find_element(By.CSS_SELECTOR, "#postal-code")
        input_postal_code.clear()
        input_postal_code.send_keys("432064")


    @allure.step("Нажатие на кнопку 'continue'")
    def click_continue_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()


    @allure.step("Получение итоговой суммы и проверка результата")
    #страница 4
    def get_total_sum(self):
        total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return total
    def result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return result


