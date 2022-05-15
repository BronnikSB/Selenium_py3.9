from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    btn_troll = browser.find_element_by_css_selector(".trollface")
    btn_troll.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value")
    input_value = x.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    input_result = browser.find_element_by_id("answer")
    input_result.send_keys(calc(input_value))

    btn_sub = browser.find_element_by_css_selector(".btn")
    btn_sub.click()

finally:
    time.sleep(10)
    browser.quit()