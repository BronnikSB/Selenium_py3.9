import pytest
from selenium import webdriver
import time
import math




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestClass01():
    @pytest.mark.parametrize('language', ['236895', '236896', '236897', '236898',
                             '236899', '236903', '236904', '236905'])
    def test_guest_should_see_login_link(self, browser, language):
        link = f"https://stepik.org/lesson/{language}/step/1"
        browser.get(link)
        input_text = browser.find_element_by_tag_name('textarea')
        answer = math.log(int(time.time()))
        input_text.send_keys(str(answer))
        btn_push = browser.find_element_by_css_selector('.submit-submission')
        btn_push.click()
        check_final = browser.find_elements_by_tag_name('pre')
        text_check_final = check_final[0].text
        assert 'Correct!' == text_check_final