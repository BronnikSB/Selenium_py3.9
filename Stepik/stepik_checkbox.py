from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.maximize_window()


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    input_x = browser.find_element_by_id("answer")
    check_robot = browser.find_element_by_id('robotCheckbox')
    radio_robot = browser.find_element_by_id('robotsRule')
    btn_sub = browser.find_element_by_css_selector(".btn")

    # достаем значение атрибуда
    x = x_element.get_attribute('valuex')
    # Считаем математическую функцию
    total_x = calc(x)
    # Вводим результат
    input_x.send_keys(total_x)
    # Ставим чек-бокс
    check_robot.click()
    # Выбираем нужную радио-кнопку
    radio_robot.click()
    # Кликаем на кнопку подтвеждения
    time.sleep(1)
    btn_sub.click()

finally:
    time.sleep(10)
    browser.quit()


