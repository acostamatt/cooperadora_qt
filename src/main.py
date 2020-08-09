import sys

from PyQt5.QtWidgets import QApplication

from controllers.form_socio import FormSocioController
from controllers.login import LoginController
from controllers.main_window import MainWindowController
from models.dbcon import DB
from views.socio.form_socio import FormSocio
from views.login.login import Login
from views.main_window.main_window import MainWindow

class App(QApplication):
    def __init__(self):
        QApplication.__init__(self, sys.argv)
        self.show_form_login()
        DB().conectar()
        #self.show_main_window()
        #self.show_form_socio_window()

    def show_form_login(self):
        self.form_login = LoginController(Login(),MainWindow())
        self.form_login.show_view()

    def show_main_window(self):
        self.main_window = MainWindowController(MainWindow())
        self.main_window.show_view()

    def show_form_socio_window(self):
        self.form_socio = FormSocioController(FormSocio())
        self.form_socio.show_view()

app = App()
sys.exit(app.exec_())