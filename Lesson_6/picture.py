from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

#Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

#Дождитесь загрузки всех картинок.
waiter = WebDriverWait(driver, 40, 0.1)
waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))

#Получите значение атрибута src у 3-й картинки.
image_container = driver.find_element(By.CSS_SELECTOR, "#image-container")
src_attribute = image_container.find_element(By.CSS_SELECTOR, "img#award").get_attribute("src")

#Выведите значение в консоль
print(src_attribute)