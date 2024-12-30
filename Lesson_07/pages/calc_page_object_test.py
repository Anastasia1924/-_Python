from selenium import webdriver

from pages.CalcPage import CalcPage

def test_45_seconds():
    driver = webdriver.Chrome()

    calc_page = CalcPage(driver)

    calc_page.open_calc()
    calc_page.fill_form("45")
    calc_page.click_button_7()
    calc_page.click_button_plus()
    calc_page.click_button_8()
    calc_page.click_button_sum()
    result = calc_page.get_result()

    assert int(result) == 15

    driver.quit()



