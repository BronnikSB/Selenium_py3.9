from atf.ui import *
from inside.pages_inside.edo_controls.edo3dialog import Edo3Dialog
from inside.pages_inside.edo_controls.saby_page import MasterDetail
from atf.ui.controls_vdom.vdom_controls_popup_confirmation import ControlsPopupConfirmation


class CreateMilestone(MasterDetail):
    menu_btn = ControlsButton(icon='icon-RoundPlus')
    document = Element(By.CSS_SELECTOR, '[template="PM/Milestones/dialog:Dialog"]')
    btn_milestone = ControlsListView()
    document_mi = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Grid_support-ladder', 'Таблица вехи')
    confirm_btn = ControlsPopupConfirmation()

    def create(self):
        self.add('Выпуск релиза')

    def open_save_milestone(self):
        self.search_and_open('Test 007')

    def delete_mil(self):
        self.search('Test 007')
        self.document_mi.row(contains_text='Test 007').select_menu_actions('Удалить')
        self.confirm_btn.select(button_text='Да')


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
