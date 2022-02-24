from atf.ui import *
from Auth.auth_page import *
from CreateMilestone.main import *
from atf.core import run_tests


class TestCreateMilestone(TestCaseUI):
    @classmethod
    def setup_class(cls):
        cls.browser.open('https://fix-online.sbis.ru/page/milestones')
        AuthPage(cls.driver).auth('Демо_тензор', 'Демо123')

    def test_01(self):
        milestone_create = CreateMilestone(self.driver)
        milestone_dialog = MilestoneDialog(self.driver)
        milestone_create.create()
        milestone_dialog.fill_milestone()
        milestone_dialog.save_milestone()

    def test_02(self):
        milestone_create = CreateMilestone(self.driver)
        milestone_dialog = MilestoneDialog(self.driver)
        milestone_create.open_save_milestone()
        milestone_dialog.check_save()
        milestone_dialog.new_tab()

    def teardown(self):
        self.browser.close_windows_and_alert()


if __name__ == '__main__':
    run_tests()