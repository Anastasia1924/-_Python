from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()

    def open_form(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main")))

    def send_first_name(self, first_name):
        self._driver.find_element(By.NAME, "first-name").send_keys(first_name)

    def send_last_name(self, last_name):
        self._driver.find_element(By.NAME, "last-name").send_keys(last_name)

    def send_address(self, address):
        self._driver.find_element(By.NAME, "address").send_keys(address)

    def send_mail(self, e_mail):
        self._driver.find_element(By.NAME, "e-mail").send_keys(e_mail)

    def send_phone(self, phone):
        self._driver.find_element(By.NAME, "phone").send_keys(phone)

    def send_zip_code(self, zip_code):
        self._driver.find_element(By.NAME, "zip-code").send_keys(zip_code)

    def send_city(self, city):
        self._driver.find_element(By.NAME, "city").send_keys(city)

    def send_country(self, country):
        self._driver.find_element(By.NAME, "country").send_keys(country)

    def send_job(self, job_position):
        self._driver.find_element(By.NAME, "job-position").send_keys(job_position)

    def send_company(self, company):
        self._driver.find_element(By.NAME, "company").send_keys(company)

    def click_submit_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main")))