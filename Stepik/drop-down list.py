from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    sum_num = int(num2.text) + int(num1.text)

    value_lst = Select(browser.find_element_by_id("dropdown"))
    value_lst.select_by_value(str(sum_num))

    btn = browser.find_element_by_css_selector(".btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
