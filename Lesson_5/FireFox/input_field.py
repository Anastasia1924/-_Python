from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

# Откройте страницу http://the-internet.herokuapp.com/inputs.
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

# Введите в поле текст 1000
field_input = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/input")
field_input.send_keys("1000")
print("1000")
sleep(3)

# Очистите это поле (метод clear)
field_input.clear()

# Введите в это же поле текст 999
field_input.send_keys("999")
print("999")
sleep(3)

driver.quit()

