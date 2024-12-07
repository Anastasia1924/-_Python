from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver


# открыть страницу http://uitestingplayground.com/classattr.
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
# кликнуть на синюю кнопку
button = driver.find_element(By.CLASS_NAME, "btn.class2.btn-primary.btn-test")
button.click()
sleep(5)
# запустить скрипт три раза подряд. Убедитесь, что он отработает одинаково. Ручной запуск скрипта, цикл в коде не нужен.
# Отрабатывает нестабильно. Запущен 3 раза. 2 раза сработал одинаково, на третий вылетел.