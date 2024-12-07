# открыть страницу http://the-internet.herokuapp.com/add_remove_elements/.

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# 5 раз кликнуть на кнопку Add Element
button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button")
for x in range(5):
 button.click()

# собрать со страницы список кнопок Delete
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(len(delete_buttons))
# вывести на экран размер списка

sleep(5)