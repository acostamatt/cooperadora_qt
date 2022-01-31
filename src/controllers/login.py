from PyQt5.QtCore import QObject, pyqtSignal

from models.usuario import UserThread
from views.login.login import Login
from views.main_window.main_window import MainWindow


class LoginController(QObject):
    loginUser = pyqtSignal()

    def __init__(self, view: Login):
        QObject.__init__(self)
        self.__view_login = view
        self.__server_user = UserThread()
        self.__view_login.login_confirmado.connect(self.__on_login_confirmado)
        self.__view_login.change_check_view.connect(self.__on_change_check_view)
        self.errores = []

    def __on_change_check_view(self, check_view_pass):

        if check_view_pass == True:
            self.__view_login.mostrar_pass()
        else:
            self.__view_login.ocultar_pass()

    def __on_login_confirmado(self, user, passw):
        if user == "" or passw == "":
            self.errores.append("Debe ingresar usuario y contraseña.")
            self.__view_login.mostrar_errores(self.errores)
            self.errores[:] = []
        else:
            self.__server_user.check_user_data(user, passw)
            self.__server_user.checkUser.connect(self.__on_checked_user)
            self.__server_user.start()

    def __on_checked_user(self, msj_error):
        if msj_error != "":
            self.errores.append(msj_error)
            self.__view_login.mostrar_errores(self.errores)
            self.errores[:] = []
        else:
            self.loginUser.emit()
            self.__view_login.close()

    def show_view(self):
        self.__view_login.show()
