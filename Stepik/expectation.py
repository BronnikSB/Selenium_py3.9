from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from function import calc

browser = webdriver.Chrome()
browser.maximize_window()
# browser.implicitly_wait(30)

try:
    browser.get(" http://suninjuly.github.io/explicit_wait2.html")
    price_house = WebDriverWait(browser, 50).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn_book = browser.find_element_by_id("book")
    btn_book.click()

    x = browser.find_element_by_id("input_value")
    input_value = x.text
    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(calc(input_value))

    btn_sub = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn_sub)
    btn_sub.click()


finally:
    time.sleep(10)
    browser.quit()
