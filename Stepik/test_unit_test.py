from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()


class TestUnit(unittest.TestCase):

    def test_01(self):
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
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # находим элемент, содержащий текст

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "КУКУ")

    def test_02(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # находим элемент, содержащий текст

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "КУКУ")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        browser.quit()


if __name__ == "__main__":
    unittest.main()