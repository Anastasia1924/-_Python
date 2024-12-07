from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

# В модальном окне нажмите на кнопку Сlose
close_button = driver.find_element(By.XPATH,"(//p[normalize-space()='Close'])[1]")
sleep(3)
close_button.click()

driver.quit()


