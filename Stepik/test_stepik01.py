from selenium import webdriver
import pytest
import time
import math


answer = math.log(int(time.time()))


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLesson1():

    @pytest.mark.parametrize('link', ['236895'])
    def test_lesson3(self, browser, link):
        lesson_1 = f'https://stepik.org/lesson/{link}/step/1'
        browser.get(lesson_1)
        self.input_text = browser.find_elements_by_class_name('attempt')
        self.input_text.send_keys('fdfsad')
        btn = browser.find_element_by_class_name('submit-submission')
        btn.click()