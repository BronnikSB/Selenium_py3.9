# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
#
# try:
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

##--------------------------------------------------------------------------
# import math
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/find_link_text'
#
# try:
#     browser.get(link)
#     link_text = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     link_text.click()
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()

##--------------------------------------------------------------------------

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
#
# try:
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла
##--------------------------------------------------------------------------

# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
# browser = webdriver.Chrome()
#
# try:
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath('//form/div[6]/button[3]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

##--------------------------------------------------------------------------

from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    first_name = browser.find_element_by_css_selector('.first_block .first')
    last_name = browser.find_element_by_css_selector('.first_block .second')
    mail_name = browser.find_element_by_css_selector('.first_block .third')
    button = browser.find_element_by_css_selector("button.btn")

    first_name.send_keys("Ivan")
    last_name.send_keys("Ivanov")
    mail_name.send_keys("ivan@mail.ru")
    button.click()

    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()