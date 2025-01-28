import allure
from selenium import webdriver
from Lesson_10.pages.FormPage import FormPage


@allure.epic("Allure тесты")
@allure.title("Заполнение формы с пустым полем")
@allure.feature("Заполнение формы")
@allure.description("Незаполненное поле подсвечивается красные, а остальные зелёным")
@allure.severity("Critical")
def test_page_object():
    with allure.step("Открытие формы(переход на страницу)"):
      driver = webdriver.Chrome()
      form_page = FormPage(driver)
      form_page.open_form()

    with allure.step("Заполнение поля 'first-name'"):
      form_page.send_first_name("Иван")

    with allure.step("Заполнение поля 'last-name'"):
      form_page.send_last_name("Петров")

    with allure.step("Заполнение поля 'address'"):
      form_page.send_address("Ленина, 55-3")

    with allure.step("Заполнение поля 'e-mail'"):
      form_page.send_mail("test@skypro.com")

    with allure.step("Заполнение поля 'phone'"):
      form_page.send_phone("+7985899998787")

    with allure.step("Поле 'zip-code' остаётся пустым"):
      form_page.send_zip_code("")

    with allure.step("Заполнение поля 'city'"):
      form_page.send_city("Москва")

    with allure.step("Заполнение поля 'country'"):
      form_page.send_country("Россия")

    with allure.step("Заполнение поля 'job-position'"):
      form_page.send_job("QA")

    with allure.step("Заполнение поля 'company'"):
      form_page.send_company("SkyPro")

    with allure.step("Нажатие на кнопку 'submit'"):
      form_page.click_submit_button()

    with allure.step("Получение и проверка поля 'zip-code', что оно подсвечивается красным "):
      zip_code_field = form_page.get_class_red()
    assert "alert-danger" in zip_code_field

    with allure.step("Получение зелёных полей и проверка, что их 9"):
      green_fields = form_page.get_class_green()
    assert len(green_fields) == 9

    with allure.step("Закрытие браузера"):
      driver.quit()