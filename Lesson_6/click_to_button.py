from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#Перейдите на страницу http://uitestingplayground.com/ajax
driver.get("http://uitestingplayground.com/ajax")

#Нажмите на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
waiter = WebDriverWait(driver, 30, 0.1)
#Получите текст из зеленой плашки.
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".bg-success"), "Data loaded with AJAX get request.")
)
#Выведите его в консоль ("Data loaded with AJAX get request.")
print(driver.find_element(By.CSS_SELECTOR,"#content").text)

driver.quit()



