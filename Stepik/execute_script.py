from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get("http://SunInJuly.github.io/execute_script.html")

    x = browser.find_element_by_id("input_value")
    input_value = int(x.text)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    total_x = calc(input_value)

    btn = browser.find_element_by_css_selector(".btn")

    text_input = browser.find_element_by_id("answer")
    text_input.send_keys(total_x)

    checkbox_robot = browser.find_element_by_id("robotCheckbox")
    checkbox_robot.click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    radio_robot = browser.find_element_by_id("robotsRule")
    radio_robot.click()

    btn.click()

finally:
    time.sleep(10)
    browser.quit()