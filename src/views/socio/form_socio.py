import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal

from models.list_alumno_model import ListGradoModel, ListTurnoModel, ListDivisionModel
from views.socio.form_socio_base import Ui_FormSocio
from views.main_window.form_window_default import Ui_FormDefault

class FormSocio(QtWidgets.QWidget):
    saveSocioData = pyqtSignal((dict,))
    dniSocio = pyqtSignal((str,))
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_FormSocio()
        self.setup()

    def set_list_grado_model(self, model):
        self.ui.comboBoxGrado.setModel(model)

    def set_list_turno_model(self, model):
        self.ui.comboBoxTurno.setModel(model)

    def set_list_division_model(self, model):
        self.ui.comboBoxDivision.setModel(model)

    def setup(self):
        self.ui.setupUi(self)

        self.list_model_grado = ListGradoModel()
        self.list_model_turno = ListTurnoModel()
        self.list_model_division = ListDivisionModel()

        self.set_list_grado_model(self.list_model_grado)
        self.set_list_turno_model(self.list_model_turno)
        self.set_list_division_model(self.list_model_division)

        self.save_new_lumno = False

        self.ui.botonAgregarOtroAlumno.clicked.connect(self.clickedSaveNewAlumno)
        self.ui.lineEditDNISocio.returnPressed.connect(self.returnPressedDniSocio)
        self.ui.checkBox.stateChanged.connect(self.changeCheckBox)

    def changeCheckBox(self):
        self.statusCheckBox = self.ui.checkBox.isChecked()
        if self.statusCheckBox == True and self.ui.lineEditDNISocio.text() != '':
            self.set_status_widget_socio(True)
        elif self.statusCheckBox == False and self.ui.lineEditDNISocio.text() != '':
            self.set_status_widget_socio(False)

    def clickedSaveSocio(self):
        #print(self.ui.comboBoxTurno.currentText(), self.ui.comboBoxTurno.currentData())
        self.dict_socio = dict()
        self.dict_socio['dni_socio'] = self.ui.lineEditDNISocio.text()
        self.dict_socio['apellido_socio'] = self.ui.lineEditApellidoSocio.text()
        self.dict_socio['nombre_socio'] = self.ui.lineEditNombreSocio.text()
        self.dict_socio['domicilio_socio'] = self.ui.lineEditDomicilioSocio.text()
        self.dict_socio['telefono_socio'] = self.ui.lineEditTelSocio.text()

        self.dict_socio['dni_alumno'] = self.ui.lineEditDNIAlumno.text()
        self.dict_socio['apellido_alumno'] = self.ui.lineEditApellidoAlumno.text()
        self.dict_socio['nombre_alumno'] = self.ui.lineEditNombreAlumno.text()
        self.dict_socio['grado'] = self.ui.comboBoxGrado.currentText()
        self.dict_socio['division'] = self.ui.comboBoxDivision.currentText()
        self.dict_socio['turno'] = self.ui.comboBoxTurno.currentText()
        self.dict_socio['ciclo'] = time.strftime("%Y")
        self.dict_socio['is_update'] = self.ui.checkBox.isChecked()
        self.saveSocioData.emit(self.dict_socio)

    def clickedSaveNewAlumno(self):
        self.clickedSaveSocio()
        self.save_new_lumno = True

    def clickedExitFormSocio(self):
        self.set_status_widget_socio(True)
        self.clean_data_socio()
        self.ui.labelMsjSocio.setText('')
        self.deleteLater()

    def returnPressedDniSocio(self):
        self.dniSocio.emit(self.ui.lineEditDNISocio.text())

    def set_msj_save_socio(self,msj):
        self.ui.checkBox.setChecked(False)
        if self.save_new_lumno == True and msj == '':
            self.ui.lineEditDNIAlumno.setText('')
            self.ui.lineEditApellidoAlumno.setText('')
            self.ui.lineEditNombreAlumno.setText('')
            self.ui.comboBoxGrado.setCurrentIndex(0)
            self.ui.comboBoxTurno.setCurrentIndex(0)
            self.ui.comboBoxDivision.setCurrentIndex(0)
            mensaje = "<div style='color:#3B83BD'><strong>Complete datos del nuevo alumno.</strong></div>"
            self.ui.labelMsjSocio.setText('')
            self.ui.labelMsjSocio.setText(mensaje)
            self.ui.lineEditDNIAlumno.setFocus()
            self.save_new_lumno = False
        elif msj == '':
           self.ui.lineEditDNISocio.setText('')
           self.ui.lineEditApellidoSocio.setText('')
           self.ui.lineEditNombreSocio.setText('')
           self.ui.lineEditDomicilioSocio.setText('')
           self.ui.lineEditTelSocio.setText('')

           self.ui.lineEditDNIAlumno.setText('')
           self.ui.lineEditApellidoAlumno.setText('')
           self.ui.lineEditNombreAlumno.setText('')
           self.ui.comboBoxGrado.setCurrentIndex(0)
           self.ui.comboBoxTurno.setCurrentIndex(0)
           self.ui.comboBoxDivision.setCurrentIndex(0)
           mensaje_exito = "<div style='color:#008F39'><strong>Datos guardados correctamente.</strong></div>"
           self.ui.labelMsjSocio.setText('')
           self.ui.labelMsjSocio.setText(mensaje_exito)
           self.set_status_widget_socio(True)
        else:
            mensaje_error = f"<div style='color:#FF0000'><strong>{msj}</strong></div>"
            self.ui.labelMsjSocio.setText('')
            self.ui.labelMsjSocio.setText(mensaje_error)

    def set_data_socio(self, data_socio: dict):
        self.ui.lineEditApellidoSocio.setText(data_socio['apellido'])
        self.ui.lineEditNombreSocio.setText(data_socio['nombre'])
        self.ui.lineEditDomicilioSocio.setText(data_socio['domicilio'])
        self.ui.lineEditTelSocio.setText(str(data_socio['telefono']))
        self.ui.lineEditDNIAlumno.setText('')
        self.ui.lineEditApellidoAlumno.setText('')
        self.ui.lineEditNombreAlumno.setText('')
        self.ui.comboBoxGrado.setCurrentIndex(0)
        self.ui.comboBoxTurno.setCurrentIndex(0)
        self.ui.comboBoxDivision.setCurrentIndex(0)
        mensaje = "<div style='color:#3B83BD'><strong>Complete datos del alumno.</strong></div>"
        self.ui.labelMsjSocio.setText('')
        self.ui.labelMsjSocio.setText(mensaje)
        self.save_new_lumno = False
        self.set_status_widget_socio(False)
        self.ui.lineEditDNIAlumno.setFocus()

    def set_status_widget_socio(self, status: bool):
        self.ui.lineEditDNISocio.setEnabled(status)
        self.ui.lineEditApellidoSocio.setEnabled(status)
        self.ui.lineEditNombreSocio.setEnabled(status)
        self.ui.lineEditDomicilioSocio.setEnabled(status)
        self.ui.lineEditTelSocio.setEnabled(status)

    def clean_data_socio(self):
        self.ui.lineEditDNISocio.setText('')
        self.ui.lineEditApellidoSocio.setText('')
        self.ui.lineEditNombreSocio.setText('')
        self.ui.lineEditDomicilioSocio.setText('')
        self.ui.lineEditTelSocio.setText('')

        self.ui.lineEditDNIAlumno.setText('')
        self.ui.lineEditApellidoAlumno.setText('')
        self.ui.lineEditNombreAlumno.setText('')
        self.ui.comboBoxGrado.setCurrentIndex(0)
        self.ui.comboBoxTurno.setCurrentIndex(0)
        self.ui.comboBoxDivision.setCurrentIndex(0)

class FormSocioDefault(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_FormDefault()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)