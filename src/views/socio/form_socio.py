from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton

from views.base.form_socio_base import Ui_FormSocio
from views.base.table_window_default import Ui_TableDefault

class FormSocio(QtWidgets.QWidget):
    saveSocioData = pyqtSignal((dict,))

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_FormSocio()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)
        self.set_icon_button(self.ui.saveSocio,'../assets/icons/feather/save.svg')
        self.set_icon_button(self.ui.botonSalir,'../assets/icons/feather/x.svg')

    def clickedSaveSocio(self):
        # print(self.ui.lineEditDNISocio.text())
        self.dict_socio = dict()
        self.dict_socio['dni_socio'] = self.ui.lineEditDNISocio.text()
        self.dict_socio['apellido_socio'] = self.ui.lineEditApellidoSocio.text()
        self.dict_socio['nombre_socio'] = self.ui.lineEditNombreSocio.text()
        self.dict_socio['domicilio_socio'] = self.ui.lineEditDomicilioSocio.text()
        self.dict_socio['telefono_socio'] = self.ui.lineEditTelSocio.text()

        self.saveSocioData.emit(self.dict_socio)

    def clickedExitFormSocio(self):
        self.ui.labelMsjSocio.setText('')
        self.deleteLater()

    def set_msj_save_socio(self,msj):
        if msj == '':
           self.ui.lineEditDNISocio.setText('')
           self.ui.lineEditApellidoSocio.setText('')
           self.ui.lineEditNombreSocio.setText('')
           self.ui.lineEditDomicilioSocio.setText('')
           self.ui.lineEditTelSocio.setText('')

           mensaje_exito = "<div style='color:#008F39'><strong>Datos guardados correctamente.</strong></div>"
           self.ui.labelMsjSocio.setText('')
           self.ui.labelMsjSocio.setText(mensaje_exito)
        else:
            mensaje_error = f"<div style='color:#FF0000'><strong>{msj}</strong></div>"
            self.ui.labelMsjSocio.setText('')
            self.ui.labelMsjSocio.setText(mensaje_error)

    def set_data_socio(self, data_socio: dict):
        self.ui.lineEditApellidoSocio.setText(data_socio['apellido'])
        self.ui.lineEditNombreSocio.setText(data_socio['nombre'])
        self.ui.lineEditDomicilioSocio.setText(data_socio['domicilio'])
        self.ui.lineEditTelSocio.setText(str(data_socio['telefono']))

    def set_icon_button(self, buttonIcon: QPushButton, urlIcon):
        buttonIcon.setIcon(QtGui.QIcon(urlIcon))
        buttonIcon.setIconSize(QtCore.QSize(20, 20))
        buttonIcon.setGeometry(QtCore.QRect(1030, 500, 161, 61))

    def clean_data_socio(self):
        self.ui.lineEditDNISocio.setText('')
        self.ui.lineEditApellidoSocio.setText('')
        self.ui.lineEditNombreSocio.setText('')
        self.ui.lineEditDomicilioSocio.setText('')
        self.ui.lineEditTelSocio.setText('')

class FormSocioDefault(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_TableDefault()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)