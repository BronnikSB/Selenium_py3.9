from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Sergey")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Bronnik")

    mail = browser.find_element_by_name("email")
    mail.send_keys("srg@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test1.txt"
    file_path = os.path.join(current_dir, file_name)

    load_btn = browser.find_element_by_id("file")
    load_btn.send_keys(file_path)

    btn_sub = browser.find_element_by_css_selector(".btn")
    btn_sub.click()

finally:
    time.sleep(10)
    browser.quit()