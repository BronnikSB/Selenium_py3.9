from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
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