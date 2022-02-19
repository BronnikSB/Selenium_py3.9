from atf import *

from atf.core import run_tests
from atf.ui import *
from TestAddVeh.page.auth_page import AuthPage
from TestAddVeh.page.main_page import Milestone


class TestAddMilestone(TestCaseUI):
    @classmethod
    def setup_class(cls):
        cls.browser.open('https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/')
        AuthPage(cls.driver).auth('Демо_тензор', 'Демо123')

    def setup(self):
        Milestone(self.driver).plan_page()

    def test_01_openPage_milestone(self):
        Milestone(self.driver).check_open()

    def test_02_check_save_milestone(self):
        Milestone(self.driver).check_save()
        # Milestone(self.driver).new_tab()

    def test_03_newTab(self):
        Milestone(self.driver).new_tab()

    def teardown(self):
        self.browser.close_windows_and_alert()


if __name__ == '__main__':
    run_tests()