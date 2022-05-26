""" Покрывает функционал  'Создание Вехи' ...ссылка на проверку..."""
from PageObject.Auth.auth_page import *
from PageObject.main import *
from inside.pages_inside.api.milestone import *


class TestCreateMilestone(TestCaseUI):
    """ Создание и открытие в новой вкладке документа 'Веха' """
    @classmethod
    def setup_class(cls):
        cls.browser.open('https://fix-online.sbis.ru/page/milestones')
        AuthPage(cls.driver).auth('Демо_тензор', 'Демо123')

    def test_01(self):
        """Создаем, заполняем и сохраняем документ"""
        log('Создание документа')
        milestone_create = CreateMilestone(self.driver)
        milestone_dialog = MilestoneDialog(self.driver)
        milestone_create.create()
        milestone_dialog.fill_milestone()
        milestone_dialog.save_milestone()

    def test_02(self):
        """Открываем документ из реестра.
        Проверяем открытие в новой вкладке"""
        log('Открытие в новой вкладке')
        milestone_create = CreateMilestone(self.driver)
        milestone_dialog = MilestoneDialog(self.driver)
        milestone_create.open_save_milestone()
        milestone_dialog.check_save()
        milestone_dialog.new_tab()

    def test_03(self):
        """Удаляем созданную веху"""
        log('Удаление вехи')
        milestone_create = CreateMilestone(self.driver)
        milestone_create.delete_mil()

    def teardown(self):
        self.browser.close_windows_and_alert()


if __name__ == '__main__':
    run_tests()