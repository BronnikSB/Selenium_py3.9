from atf.ui import *
from inside.pages_inside.edo_controls.edo3dialog import Edo3Dialog
# from inside.pages_inside.edo_controls.saby_page import MasterDetail
from inside.pages_inside.edo_controls.saby_page import MasterDetail


class CreateMilestone(MasterDetail):
    menu_btn = ControlsButton(icon='icon-RoundPlus')
    document = Element(By.CSS_SELECTOR, '[template="PM/Milestones/dialog:Dialog"]')
    btn_milestone = ControlsListView()

    def create(self):
        self.add('Выпуск релиза')

    def open_save_milestone(self):
        self.search_and_open('Test 007')


@templatename('PM/Milestones/dialog:Dialog')
class MilestoneDialog(Edo3Dialog):
    name_milestone = ControlsInputText(By.CSS_SELECTOR, '.ms-SecondLineContent__name')
    description_milestone = ControlsInputArea(By.CSS_SELECTOR, '.ms-SecondLineContent__descriptionContainer')

    def fill_milestone(self):
        self.name_milestone.type_in(string='Test 007')
        self.description_milestone.type_in(string='Description 007')

    def check_save(self):
        self.name_milestone.should_be(ExactText('Test 007'))
        self.description_milestone.should_be(ExactText('Description 007'))

    def new_tab(self):
        self.select_service_command('Ссылка', 'Открыть в новой вкладке')
        self.check_open()
        self.name_milestone.should_be(ExactText('Test 007'))
        self.description_milestone.should_be(ExactText('Description 007'))

    def save_milestone(self):
        self.save()
