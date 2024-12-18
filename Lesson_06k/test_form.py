import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form(driver):
    #Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    #Заполните форму значениями
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.clear()
    first_name.send_keys("Иван")
    last_name = driver.find_element(By.NAME, "last-name")
    last_name.clear()
    last_name.send_keys("Петров")
    address = driver.find_element(By.NAME, "address")
    address.clear()
    address.send_keys("Ленина, 55-3")
    mail = driver.find_element(By.NAME, "e-mail")
    mail.clear()
    mail.send_keys("test@skypro.com")
    phone = driver.find_element(By.NAME, "phone")
    phone.clear()
    phone.send_keys("+7985899998787")
    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.clear()
    zip_code.send_keys("")
    city = driver.find_element(By.NAME, "city")
    city.clear()
    city.send_keys("Москва")
    country = driver.find_element(By.NAME, "country")
    country.clear()
    country.send_keys("Россия")
    job = driver.find_element(By.NAME, "job-position")
    job.clear()
    job.send_keys("QA")
    company = driver.find_element(By.NAME, "company")
    company.clear()
    company.send_keys("SkyPro")
    #Нажмите кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger")))

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")

    # Проверьте(assert), что поле Zip code подсвечено красным
    assert "alert-danger" in zip_code_field.get_attribute("class")
    # Проверьте (assert), что остальные поля подсвечены зеленым.
    green_fields = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
    assert len(green_fields) == 9



