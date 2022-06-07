import time
from selenium.webdriver.common.by import By


# Проверка наличия кнопки добаления в корзину.
def test_interface_lang(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    btn_add_to_basket = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form", "Добавить в корзину")
    assert len(btn_add_to_basket) > 0
    time.sleep(15)
