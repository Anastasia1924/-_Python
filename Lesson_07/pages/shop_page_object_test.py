from selenium import webdriver


from pages.ShopPage import ShopPage


def test_total_sum():
    driver = webdriver.Chrome()

    shop_page = ShopPage(driver)

    shop_page.open_authorization()
#страница 1
    shop_page.input_login("standard_user")
    shop_page.input_password("secret_sauce")
    shop_page.click_login_button()
#страница 2
    shop_page.add_items_to_cart()
    shop_page.go_in_cart()
    shop_page.click_checkout_button()
#страница 3
    shop_page.input_first_name("Anastasiia")
    shop_page.input_last_name("Gosteeva")
    shop_page.input_postal_code("432064")
    shop_page.click_continue_button()
#траница 4
    shop_page.get_total_sum()
    result = shop_page.result()

    assert result == "Total: $58.29"


    driver.quit()