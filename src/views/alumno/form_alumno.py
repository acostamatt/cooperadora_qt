from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QPushButton

from models.combo_box_extend import ExtendedComboBox
from models.list_alumno_model import (
    ListDivisionModel,
    ListGradoModel,
    ListSocioModel,
    ListTurnoModel,
)
from views.base.form_alumno_base import Ui_FormAlumno
from views.base.table_window_default import Ui_TableDefault


class FormAlumno(QtWidgets.QWidget):
    saveAlumnoData = pyqtSignal((dict,))

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_FormAlumno()
        self.setup()

    def set_filter_socio_model(
        self, model: ListSocioModel, combo_box_socio: ExtendedComboBox
    ):
        model.insert_data(self.combo_box_socio)
        self.ui.horizontalLayout_3.addWidget(combo_box_socio)

    def set_list_grado_model(self, model):
        self.ui.comboBoxGrado.setModel(model)

    def set_list_turno_model(self, model):
        self.ui.comboBoxTurno.setModel(model)

    def set_list_division_model(self, model):
        self.ui.comboBoxDivision.setModel(model)

    def setup(self):
        self.ui.setupUi(self)

        self.list_model_socio = ListSocioModel()
        self.combo_box_socio = ExtendedComboBox()
        self.list_model_grado = ListGradoModel()
        self.list_model_turno = ListTurnoModel()
        self.list_model_division = ListDivisionModel()

        self.set_icon_button(self.ui.saveAlumno, "../assets/icons/feather/save.svg")
        self.set_icon_button(self.ui.pushButton, "../assets/icons/feather/x.svg")
        self.set_list_grado_model(self.list_model_grado)
        self.set_list_turno_model(self.list_model_turno)
        self.set_list_division_model(self.list_model_division)
        self.set_filter_socio_model(self.list_model_socio, self.combo_box_socio)
        self.combo_box_socio.setCurrentIndex(-1)
        self.ui.comboBoxTurno.setCurrentIndex(-1)
        self.ui.comboBoxGrado.setCurrentIndex(-1)
        self.ui.comboBoxDivision.setCurrentIndex(-1)

    def clickedSaveAlumno(self):
        self.dict_alumno = dict()
        self.dict_alumno["dni"] = self.ui.lineEditDNIAlumno.text()
        self.dict_alumno["apellido"] = self.ui.lineEditApellidoAlumno.text()
        self.dict_alumno["nombre"] = self.ui.lineEditNombreAlumno.text()
        self.dict_alumno["socio"] = self.combo_box_socio.currentData(Qt.UserRole)
        self.dict_alumno["grado"] = self.ui.comboBoxGrado.currentText()
        self.dict_alumno["division"] = self.ui.comboBoxDivision.currentText()
        self.dict_alumno["turno"] = self.ui.comboBoxTurno.currentText()
        self.saveAlumnoData.emit(self.dict_alumno)

    def clickedExitFormAlumno(self):
        self.ui.labelMsjAlumno.setText("")
        self.deleteLater()

    def set_msj_save_alumno(self, msj):
        if msj == "":
            self.clean_data_alumno()

            mensaje_exito = "<div style='color:#008F39'><strong>Datos guardados correctamente.</strong></div>"
            self.ui.labelMsjAlumno.setText("")
            self.ui.labelMsjAlumno.setText(mensaje_exito)
        else:
            mensaje_error = f"<div style='color:#FF0000'><strong>{msj}</strong></div>"
            self.ui.labelMsjAlumno.setText("")
            self.ui.labelMsjAlumno.setText(mensaje_error)

    def set_data_alumno(self, data_alumno: dict):
        self.ui.lineEditDNIAlumno.setText(str(data_alumno["dni"]))
        self.ui.lineEditApellidoAlumno.setText(data_alumno["apellido"])
        self.ui.lineEditNombreAlumno.setText(data_alumno["nombre"])
        self.combo_box_socio.setCurrentIndex(data_alumno["socio"])
        self.ui.comboBoxGrado.setCurrentText(str(data_alumno["grado"]))
        self.ui.comboBoxDivision.setCurrentText(data_alumno["division"])
        self.ui.comboBoxTurno.setCurrentText(data_alumno["turno"])

    def set_icon_button(self, buttonIcon: QPushButton, urlIcon):
        buttonIcon.setIcon(QtGui.QIcon(urlIcon))
        buttonIcon.setIconSize(QtCore.QSize(20, 20))
        buttonIcon.setGeometry(QtCore.QRect(1030, 500, 161, 61))

    def clean_data_alumno(self):
        self.ui.lineEditDNIAlumno.setText("")
        self.ui.lineEditApellidoAlumno.setText("")
        self.ui.lineEditNombreAlumno.setText("")
        self.combo_box_socio.setCurrentIndex(-1)
        self.ui.comboBoxGrado.setCurrentIndex(-1)
        self.ui.comboBoxDivision.setCurrentIndex(-1)
        self.ui.comboBoxTurno.setCurrentIndex(-1)


class TableAlumnoDefault(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_TableDefault()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)
