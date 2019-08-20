from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QComboBox, QSizePolicy, QCheckBox, \
    QPushButton


class Login(QWidget):
    login_confirmado = pyqtSignal(str, str)
    change_check_view = pyqtSignal(bool)
    def __init__(self):
        QWidget.__init__(self)
        self.setup()

    def setup(self):
        self.__main_layout = QHBoxLayout()
        self.__form_layout = QVBoxLayout()

        self.__main_layout.addLayout(self.__form_layout)

        self.__label_user = QLineEdit()
        self.__label_user.setPlaceholderText("Introduzca Usuario")
        self.__form_layout.addWidget(self.__label_user)

        self.__label_pass = QLineEdit()
        self.__label_pass.setPlaceholderText("Contraseña")
        self.__label_pass.setEchoMode(self.__label_pass.Password)
        self.__form_layout.addWidget(self.__label_pass)

        self.__check_view_pass = QCheckBox()
        self.__check_view_pass.setText("Mostrar contraseña")
        self.__form_layout.addWidget(self.__check_view_pass)

        self.__label_saludo = QLabel()
        self.__label_saludo.hide()
        self.__form_layout.addWidget(self.__label_saludo)

        self.__boton_guardar = QPushButton("Guardar")
        self.__form_layout.addWidget(self.__boton_guardar)

        #self.setFixedSize(self.sizeHint())

        self.setLayout(self.__main_layout)

        self.__boton_guardar.clicked.connect(self.on_enviar_click)
        self.__check_view_pass.clicked.connect(self.on_enviar_change_check_view)

    def on_enviar_click(self):
        self.login_confirmado.emit(self.__label_user.text(),
                                   self.__label_pass.text())

    def on_enviar_change_check_view(self):
        self.change_check_view.emit(self.__check_view_pass.isChecked())

    def mostrar_errores(self, errores: list):
        lista_errores = "<br>".join([f"- {msg}" for msg in errores])
        mensaje_error = f"<div><h3>Hay errores:</h3></div>" \
                        f"<div style='color:#FF0000'><strong>{lista_errores}</strong></div>"
        self.__label_saludo.setText(mensaje_error)
        self.__label_saludo.show()

    def mostrar_mensaje_exito(self, mensaje: str):
        self.__label_saludo.setText(mensaje)
        self.__label_saludo.show()

    def mostrar_pass(self):
        self.__label_pass.setEchoMode(self.__label_pass.Normal)

    def ocultar_pass(self):
        self.__label_pass.setEchoMode(self.__label_pass.Password)
