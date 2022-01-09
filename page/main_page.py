from atf.ui import *


class NotePage(Region):
    document = Element(By.CSS_SELECTOR, '[name="item-documents"]', 'Документы')
    note = Element(By.CSS_SELECTOR, '[href="/page/notes"]', 'Заметки')
    add_note = Element(By.CSS_SELECTOR, '[name="addNote"]', 'Добавить заметку')
    text = Element(By.CSS_SELECTOR, '[id="mce_0"]', 'Написать текст')
    ok_btn = Element(By.CSS_SELECTOR, '[name="okButton"]')
    lst_note = CustomList(By.CSS_SELECTOR, '.ws-note__content', 'Список заметок')
    delete_note = Element(By.CSS_SELECTOR, '[name="Remove"]', 'Удалить')
    positive_btn = Element(By.CSS_SELECTOR, '[name="positiveButton"]', 'Подтверждение')

    def note_page(self):
        self.document.click()
        self.note.click()

    def new_add_note(self):
        self.add_note.click()
        self.text.type_in('Hello world!')
        self.ok_btn.click()

    def displayed_note(self):
        self.lst_note.item(with_text='Hello world!').should_be(Displayed).click()
        self.delete_note.click()
        self.positive_btn.click()
        self.driver.refresh()
        self.lst_note.item(with_text='Hello world!').should_be(Disabled)






