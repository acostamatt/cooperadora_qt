from PyQt5 import QtCore
from PyQt5 import QtWidgets
from views.login.login_base import Ui_Form

class Login(QtWidgets.QWidget):
    login_confirmado = QtCore.pyqtSignal(str, str)
    change_check_view = QtCore.pyqtSignal(bool)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)
        #self.setFixedSize(self.sizeHint())
        self.__label_img_user = self.ui.label_img_user
        self.__check_view_pass = self.ui.check_view_pass
        self.__line_edit_pass = self.ui.line_edit_pass
        self.__boton_check = self.ui.boton_check
        self.__label_msj = self.ui.label_msj
        self.__line_edit_user = self.ui.line_edit_user
        #self.setFixedSize(self.sizeHint())
        self.__line_edit_pass.setEchoMode(self.__line_edit_pass.Password)
        self.__boton_check.clicked.connect(self.on_enviar_click)
        self.__check_view_pass.clicked.connect(self.on_enviar_change_check_view)

    def on_enviar_click(self):
        self.login_confirmado.emit(self.__line_edit_user.text(),
                                   self.__line_edit_pass.text())

    def on_enviar_change_check_view(self):
        self.change_check_view.emit(self.__check_view_pass.isChecked())

    def mostrar_errores(self, errores: list):
        lista_errores = "<br>".join([f"- {msg}" for msg in errores])
        mensaje_error = f"<div><h4>Hay errores:</h4></div>" \
                        f"<div style='color:#FF0000'><strong>{lista_errores}</strong></div>"
        self.__label_msj.setText(mensaje_error)
        self.__label_msj.setMaximumSize(500, 500)
        self.__label_msj.show()

    def mostrar_pass(self):
        self.__line_edit_pass.setEchoMode(self.__line_edit_pass.Normal)

    def ocultar_pass(self):
        self.__line_edit_pass.setEchoMode(self.__line_edit_pass.Password)

