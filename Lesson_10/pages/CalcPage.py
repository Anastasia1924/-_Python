import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Калькулятор")
class CalcPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()

    @allure.step("Открытие калькулятора(переход на страницу)")
    def open_calc(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".col-sm-12.py-10")))

    @allure.step("Заполнение формы ожидания значением {delay}")
    def fill_form(self, delay):
        input_delay = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        input_delay.clear()
        input_delay.send_keys(delay)

    @allure.step("Нажатие кнопки 7")
    def click_button_7(self):
        self._driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[1]").click()

    @allure.step("Нажатие кнопки +")
    def click_button_plus(self):
        self._driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[4]").click()

    @allure.step("Нажатие кнопки 8")
    def click_button_8(self):
        self._driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[2]").click()

    @allure.step("Нажатие кнопки =")
    def click_button_sum(self):
        self._driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[15]").click()

        waiter = WebDriverWait(self._driver, 55, 0.1)
        waiter.until(
            EC.text_to_be_present_in_element((By.XPATH, "/html/body/main/div/div[4]/div/div/div[1]/div"), "15"))

    @allure.step("Получение результата")
    def get_result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result






