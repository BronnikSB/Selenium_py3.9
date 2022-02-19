from atf.ui import *


class AuthPage(Region):

    login = Element(By.CSS_SELECTOR, '[name="login"]', 'Логин')
    password = Element(By.CSS_SELECTOR, '[name="password"]', 'Пароль')
    enter_btn = Element(By.CSS_SELECTOR, '.auth-Form__submit', 'Войти')

    def auth(self, user_login, user_password):
        self.login.type_in(user_login)
        self.password.type_in(user_password)
        self.enter_btn.click()