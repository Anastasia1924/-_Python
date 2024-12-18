import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    driver = webdriver.Chrome()
    #Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html.
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    #В поле ввода по локатору # delay введите значение 45
    delay = driver.find_element(By.CSS_SELECTOR, "input#delay")
    delay.clear()
    delay.send_keys("45")
    #Нажмите на кнопки
    driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[1]").click()
    driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[4]").click()
    driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[2]").click()
    driver.find_element(By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[15]").click()

    WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/main/div/div[4]/div/div/div[1]/div"), "15"))

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text

    #Проверьте(assert), что в окне отобразится результат 15 через 45 секунд.
    assert int(result) == 15

    driver.quit()