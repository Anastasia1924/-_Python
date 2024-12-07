from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver



# открыть страницу http://uitestingplayground.com/dynamicid.
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")
# кликнуть на синюю кнопку
button = driver.find_element(By.XPATH,"/html/body/section/div/button")
button.click()
sleep(5)
# запустить скрипт три раза подряд. Убедитесь, что он отработает одинаково. Ручной запуск скрипта, цикл в коде не нужен.
# запущен 3 раза, отрабатыает одинаково.

