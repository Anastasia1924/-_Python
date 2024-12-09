from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#Перейдите на сайт http://uitestingplayground.com/textinput.
driver.get("http://uitestingplayground.com/textinput")

#Укажите в поле ввода текст SkyPro
input_selector = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_selector.send_keys("SkyPro")
waiter = WebDriverWait(driver, 5)

#Нажмите на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()


#Получите текст кнопки и выведите в консоль ("SkyPro")
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)
#Выведите его в консоль ("Data loaded with AJAX get request.")
print(driver.find_element(By.CSS_SELECTOR,"#updatingButton").text)

driver.quit()

