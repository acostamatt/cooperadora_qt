from models.dao import LOGIN_DAO
from views.login import Login
from models.login import LoginModel

class LoginController:
    def __init__(self, view: Login):
        self.__view = view
        self.__view.login_confirmado.connect(self.__on_login_confirmado)
        self.__view.change_check_view.connect(self.__on_change_check_view)

    def __on_change_check_view(self, check_view_pass):

        if check_view_pass == True:
            self.__view.mostrar_pass()
        else:
            self.__view.ocultar_pass()

    def __on_login_confirmado(self, user, passw):

        login = LoginModel()
        login.user = user
        login.passw = passw
        errores = login.validar()

        if errores:
            self.__view.mostrar_errores(errores)
        else:
            if LOGIN_DAO.comprobar_usuario(login):
                self.__view.close()
            else:
                errores.append("No existe usuario y contraseña.")
                self.__view.mostrar_errores(errores)

    def show_view(self):
        self.__view.show()

