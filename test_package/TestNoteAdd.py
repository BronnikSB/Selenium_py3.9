from atf.core import run_tests
from atf.ui import *
from page.auth_page import AuthPage
from page.main_page import NotePage


class TestNoteAdd(TestCaseUI):
    @classmethod
    def setup_class(cls):
        cls.browser.open('https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/')
        AuthPage(cls.driver).auth('Демо_тензор', 'Демо123')

    def setup(self):
        NotePage(self.driver).note_page()

    def test_01(self):
        NotePage(self.driver).new_add_note()

    def test_02(self):
        NotePage(self.driver).displayed_note()

    def tearDown(self):
        self.browser.close_windows_and_alert()


if __name__ == '__main__':
    run_tests()