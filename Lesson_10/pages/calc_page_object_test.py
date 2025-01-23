import allure
from selenium import webdriver
from Lesson_10.pages.CalcPage import CalcPage


@allure.epic("Allure тесты")
@allure.title("Операция сложения 7+8")
@allure.feature("Калькулятор")
@allure.description("Операция сложения 7+8 с задержкой 45 секунд")
@allure.severity("Critical")
def test_45_seconds():
    with allure.step("Открыть браузер и перейти на страницу калькулятора"):
      driver = webdriver.Chrome()
      calc_page = CalcPage(driver)
      calc_page.open_calc()

    with allure.step("Установка таймера"):
      calc_page.fill_form("45")

    with allure.step("Нажатие кнопки 7"):
      calc_page.click_button_7()

    with allure.step("Нажатие кнопки +"):
      calc_page.click_button_plus()

    with allure.step("Нажатие кнопки 8"):
      calc_page.click_button_8()

    with allure.step("Нажатие кнопки ="):
      calc_page.click_button_sum()

    with allure.step("Получение и проверка результата"):
      result = calc_page.get_result()
      assert int(result) == 15

    with allure.step("Закрытие браузера"):
      driver.quit()



