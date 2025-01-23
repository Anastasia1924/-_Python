import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Заполнение формы")
class FormPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()

    @allure.step("Открытие формы(переход на страницу)")
    def open_form(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main")))

    @allure.step("Ввод имени")
    def send_first_name(self, first_name):
        self._driver.find_element(By.NAME, "first-name").send_keys(first_name)

    @allure.step("Ввод фамилии")
    def send_last_name(self, last_name):
        self._driver.find_element(By.NAME, "last-name").send_keys(last_name)

    @allure.step("Ввод адреса")
    def send_address(self, address):
        self._driver.find_element(By.NAME, "address").send_keys(address)

    @allure.step("Ввод электронной почты")
    def send_mail(self, e_mail):
        self._driver.find_element(By.NAME, "e-mail").send_keys(e_mail)

    @allure.step("Ввод номера телефона")
    def send_phone(self, phone):
        self._driver.find_element(By.NAME, "phone").send_keys(phone)

    @allure.step("Поле 'zip-code' остаётся пустым")
    def send_zip_code(self, zip_code):
        self._driver.find_element(By.NAME, "zip-code").send_keys(zip_code)

    @allure.step("Ввод названия города")
    def send_city(self, city):
        self._driver.find_element(By.NAME, "city").send_keys(city)

    @allure.step("Ввод названия страны")
    def send_country(self, country):
        self._driver.find_element(By.NAME, "country").send_keys(country)

    @allure.step("Ввод названия должности")
    def send_job(self, job_position):
        self._driver.find_element(By.NAME, "job-position").send_keys(job_position)

    @allure.step("Ввод названия компании")
    def send_company(self, company):
        self._driver.find_element(By.NAME, "company").send_keys(company)

    @allure.step("Нажатие на кнопку 'submit'")
    def click_submit_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main")))

    @allure.step("Получение поля, подсвеченного красным цветом")
    def get_class_red(self):
        zip_code_field = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        return zip_code_field

    @allure.step("Получение полей, подсвеченных зелёным цветом")
    def get_class_green(self):
        green_fields = self._driver.find_elements(By.CSS_SELECTOR, ".alert-success")
        return green_fields