from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

# Откройте страницу http://the-internet.herokuapp.com/login.
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
# В поле username введите значение tomsmith
username_input = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/div[1]/div/input")
username_input.send_keys("tomsmith")
print()

# В поле password введите значение SuperSecretPassword!
password_input = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/div[2]/div/input")
password_input.send_keys("SuperSecretPassword!")
print()
# Нажмите кнопку Login
button_login = driver.find_element(By.CLASS_NAME, "fa.fa-2x.fa-sign-in")
button_login.click()

driver.quit()
