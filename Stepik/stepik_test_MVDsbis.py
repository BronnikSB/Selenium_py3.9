from selenium import webdriver


class Auth:
    browser = webdriver.Chrome()
    login = browser.find_element_by_css_selector('[name="Login"]')
    password = browser.find_element_by_css_selector('[name="password"]')
    enter_btn = browser.find_element_by_css_selector('.auth-Form__submit')

    def __init__(self):
