from selenium import webdriver


from pages.FormPage import FormPage

def test_page_object():
    driver = webdriver.Chrome()

    form_page = FormPage

    form_page.open_form()
    form_page.send_first_name("Иван")
    form_page.send_last_name("Петров")
    form_page.send_address("Ленина, 55-3")
    form_page.send_mail("test@skypro.com")
    form_page.send_phone("+7985899998787")
    form_page.send_zip_code("")
    form_page.send_city("Москва")
    form_page.send_country("Россия")
    form_page.send_job("QA")
    form_page.send_company("SkyPro")
    form_page.click_submit_button()