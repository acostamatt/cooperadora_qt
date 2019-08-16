import sys

from PyQt5.QtWidgets import QApplication

from controllers.login import LoginController
from views.login import Login
from views.formulario_socio import FormularioSocio
class App(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.show_form_login()

    def show_form_login(self):
        self.form_login = LoginController(Login())
        self.form_login.show_view()

app = App()
sys.exit(app.exec_())