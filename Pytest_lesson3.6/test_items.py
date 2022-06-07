import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_interface_lang(browser):
    browser.get(link)
    btn_add_to_basket = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form")
    assert len(btn_add_to_basket) > 0
    time.sleep(15)
