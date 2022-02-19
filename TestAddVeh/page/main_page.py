import time

from atf.ui import *


class Milestone(Region):
    task = CustomList(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title', 'Задачи')
    plan = CustomList(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__wrapper', 'Планы и сроки')
    tabs = ControlsTabsButtons()
    menu_btn = ControlsButton(icon='icon-RoundPlus')
    document = Element(By.CSS_SELECTOR, '[template="PM/Milestones/dialog:Dialog"]')
    btn_milestone = ControlsListView()
    name_milestone = ControlsInputText()
    description_milestone = ControlsInputArea(By.CSS_SELECTOR, '.ms-SecondLineContent__descriptionContainer')
    save_btn = ControlsButton(By.CSS_SELECTOR, '[title="Сохранить"]')
    search_milestone = CustomList(By.CSS_SELECTOR, '[title="Test 007"]', 'Название вехи')
    toolbar = ControlsToolbarsView()
    toolbar_menu = ControlsMenuControl()

    def plan_page(self):
        self.task.item(with_text='Задачи').click()
        self.plan.item(with_text='Планы и сроки').click()

    def check_open(self):
        self.menu_btn.click()
        self.btn_milestone.item(with_text='Выпуск релиза').click()
        self.document.should_be(Displayed, msg="Форма не открылась", wait_time=True)
        self.name_milestone.type_in(string='Test 007')
        self.description_milestone.send_keys("Description")
        self.save_btn.click()

    def check_save(self):
        self.search_milestone.item(contains_text="Test 007").click()
        self.name_milestone.should_be(ExactText('Test 007'))
        self.description_milestone.should_be(ExactText("Description"))

    def new_tab(self):
        self.search_milestone.item(contains_text="Test 007").click()
        self.toolbar.open_menu()
        self.toolbar_menu.select('Ссылка', 'Открыть в новой вкладке')











