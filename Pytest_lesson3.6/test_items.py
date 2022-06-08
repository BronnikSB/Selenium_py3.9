import time
from selenium.webdriver.common.by import By


# Проверка наличия кнопки добаления в корзину.
def test_btn_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    btn_add_to_basket = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form")
    assert len(btn_add_to_basket) == 1
    time.sleep(15)
