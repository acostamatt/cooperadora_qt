from PyQt5 import QtCore, QtGui, QtTest, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, pyqtSignal
from PyQt5.QtWidgets import QPushButton

from models.alumno_table_model import AlumnosTableModel
from models.combo_box_extend import ExtendedComboBox
from models.list_alumno_model import (
    ListDivisionModel,
    ListGradoModel,
    ListSocioModel,
    ListTurnoModel,
)
from models.socio import Alumno, Socio
from models.socio_table_model import SociosTableModel
from views.base.form_alumno_base import Ui_FormAlumno
from views.base.form_socio_base import Ui_FormSocio
from views.base.main_window_base import Ui_MainWindow
from views.base.table_view_alumno import Ui_TableAlumno
from views.base.table_view_socio import Ui_TableSocio
from views.socio.form_socio import FormSocioDefault


class MainWindow(QtWidgets.QWidget):
    clickedNewSocio = pyqtSignal()
    clickedNewAlumno = pyqtSignal()
    clickedNewCobranza = pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.form_socio_default = FormSocioDefault()
        self.setup()
        self.ui.layoutFormSocio.addWidget(self.form_socio_default)
        self.setFixedWidth(600)

    def setup(self):
        self.ui.setupUi(self)
        self.set_icon_button(self.ui.pushButton, "../assets/icons/feather/list.svg")
        self.set_icon_button(self.ui.pushButton_6, "../assets/icons/feather/list.svg")
        self.set_icon_button(self.ui.pushButton_8, "../assets/icons/feather/list.svg")
        self.set_icon_button(self.ui.pushButton_2, "../assets/icons/feather/plus.svg")
        self.set_icon_button(self.ui.pushButton_5, "../assets/icons/feather/plus.svg")
        self.set_icon_button(self.ui.pushButton_7, "../assets/icons/feather/plus.svg")

    def set_icon_button(self, buttonIcon: QPushButton, urlIcon):
        buttonIcon.setIcon(QtGui.QIcon(urlIcon))
        buttonIcon.setIconSize(QtCore.QSize(20, 20))
        buttonIcon.setGeometry(QtCore.QRect(1030, 500, 161, 61))

    def set_change_button_text_icon(self, check_value: bool, button_check: QPushButton):
        if check_value:
            button_check.setText("Archivar")
            self.set_icon_button(button_check, "../assets/icons/feather/slash.svg")
        else:
            button_check.setText("Recuperar")
            self.set_icon_button(
                button_check, "../assets/icons/feather/check-circle.svg"
            )

    def onClickedAltaSocio(self):
        self.clickedNewSocio.emit()

    def onClickedAltaAlumno(self):
        self.clickedNewAlumno.emit()

    def onClickedConsultaSocio(self):
        self.__table_socio = TableSocio(self)
        self.__table_model_socio = SociosTableModel()
        self.cleanLayout(self.ui.layoutFormSocio)
        self.__table_socio.set_socios_table_model(self.__table_model_socio)
        self.ui.layoutFormSocio.addWidget(self.__table_socio)
        self.setFixedWidth(1000)

    def onSearchConsultaSocio(self, search_str: str, check_socio: bool):
        self.__table_socio = TableSocio(self)
        self.__table_model_socio = SociosTableModel()
        self.cleanLayout(self.ui.layoutFormSocio)
        self.__table_socio.set_socios_table_model_search(
            self.__table_model_socio, search_str, check_socio
        )
        self.ui.layoutFormSocio.addWidget(self.__table_socio)
        self.setFixedWidth(1000)

    def onClickedConsultaAlumno(self):
        self.__table_alumno = TableAlumno(self)
        self.__table_model_alumno = AlumnosTableModel()
        self.cleanLayout(self.ui.layoutFormSocio)
        self.__table_alumno.set_alumnos_table_model(self.__table_model_alumno)
        self.ui.layoutFormSocio.addWidget(self.__table_alumno)
        self.setFixedWidth(1000)

    def onSearchConsultaAlumno(self, search_str: str, check_alumno: bool):
        self.__table_alumno = TableAlumno(self)
        self.__table_model_alumno = AlumnosTableModel()
        self.cleanLayout(self.ui.layoutFormSocio)
        self.__table_alumno.set_alumnos_table_model_search(
            self.__table_model_alumno, search_str, check_alumno
        )
        self.ui.layoutFormSocio.addWidget(self.__table_alumno)
        self.setFixedWidth(1000)

    def onClickedAltaCobranza(self):
        self.clickedNewCobranza.emit()

    def cleanLayout(self, layout):
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()


class TableAlumno(QtWidgets.QWidget):
    def __init__(self, main_window: MainWindow):
        QtWidgets.QWidget.__init__(self)
        self.main_window = main_window
        self.ui = Ui_TableAlumno()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)
        self.ui.tableView.setStyleSheet("* { gridline-color: transparent }")
        self.ui.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignVCenter)
        self.alumno_table_model = AlumnosTableModel()

        # self.ui.lineEdit.setFocus(True)
        # self.ui.lineEdit.nextInFocusChain()
        self.main_window.set_icon_button(
            self.ui.updateButton, "../assets/icons/feather/edit.svg"
        )
        self.main_window.set_icon_button(
            self.ui.inactiveButton, "../assets/icons/feather/slash.svg"
        )
        self.ui.tableView.clicked.connect(self.__on_table_clicked)
        self.ui.lineEdit.returnPressed.connect(self.__on_enter_pressed_alumno)
        self.ui.checkBox.clicked.connect(self.__on_enter_pressed_alumno)

    def set_alumnos_table_model(self, model):
        self.ui.tableView.setModel(model)
        self.ui.tableView.setColumnWidth(0, 250)
        model.refresh_data()

    def set_alumnos_table_model_search(
        self, model: QAbstractTableModel, search_str: str, check_alumno: bool
    ):
        self.ui.tableView.setModel(model)
        self.ui.tableView.setColumnWidth(0, 250)
        model.refresh_data_search(search_str, check_alumno)
        self.ui.lineEdit.setText(search_str)
        self.ui.checkBox.setChecked(check_alumno)
        self.ui.lineEdit.installEventFilter(self)
        self.ui.checkBox.installEventFilter(self)
        self.main_window.set_change_button_text_icon(
            check_alumno, self.ui.inactiveButton
        )

    def __on_enter_pressed_alumno(self):
        self.main_window.onSearchConsultaAlumno(
            self.ui.lineEdit.text(), self.ui.checkBox.isChecked()
        )

    def __on_table_clicked(self, index: QModelIndex):
        self.ui.inactiveButton.setEnabled(True)
        self.ui.updateButton.setEnabled(True)
        self.id_alumno = str(index.data(Qt.UserRole))

    def clickedUpdateAlumno(self):
        self.dict_alumno = Alumno.get_alumno_id(self.id_alumno)
        self.alumno_update = AlumnoUpdateWindow(
            self.dict_alumno, self.main_window, self.ui.labelMsj
        )
        self.alumno_update.show()

    def clickedDeleteAlumno(self):

        self.msj = Alumno.delete_alumno(self.id_alumno)
        if self.ui.checkBox.isChecked():
            self.msj = f"<div style='color:#FF0000'><strong>{self.msj}</strong></div>"
        else:
            self.msj = f"<div style='color:#008F39'><strong>{self.msj}.</strong></div>"

        self.ui.labelMsj.setText(self.msj)
        QtTest.QTest.qWait(800)

        self.main_window.onClickedConsultaAlumno()


class TableSocio(QtWidgets.QWidget):
    def __init__(self, main_window: MainWindow):
        QtWidgets.QWidget.__init__(self)
        self.main_window = main_window
        self.ui = Ui_TableSocio()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)
        self.ui.tableView.setStyleSheet("* { gridline-color: transparent }")
        self.ui.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignVCenter)
        self.socio_table_model = SociosTableModel()

        self.main_window.set_icon_button(
            self.ui.updateButton, "../assets/icons/feather/edit.svg"
        )
        self.main_window.set_icon_button(
            self.ui.inactiveButton, "../assets/icons/feather/slash.svg"
        )

        self.ui.tableView.clicked.connect(self.__on_table_clicked)
        self.ui.lineEdit.returnPressed.connect(self.__on_enter_pressed_socio)
        self.ui.checkBox.clicked.connect(self.__on_enter_pressed_socio)

    def set_socios_table_model(self, model: QAbstractTableModel):
        self.ui.tableView.setModel(model)
        self.ui.tableView.setColumnWidth(0, 250)
        model.refresh_data()

    def set_socios_table_model_search(
        self, model: QAbstractTableModel, search_str: str, check_socio: bool
    ):
        self.ui.tableView.setModel(model)
        self.ui.tableView.setColumnWidth(0, 250)
        model.refresh_data_search(search_str, check_socio)
        self.ui.lineEdit.setText(search_str)
        self.ui.checkBox.setChecked(check_socio)
        self.ui.lineEdit.installEventFilter(self)
        self.ui.checkBox.installEventFilter(self)
        self.main_window.set_change_button_text_icon(
            check_socio, self.ui.inactiveButton
        )

    def __on_enter_pressed_socio(self):
        self.main_window.onSearchConsultaSocio(
            self.ui.lineEdit.text(), self.ui.checkBox.isChecked()
        )

    def __on_table_clicked(self, index: QModelIndex):
        self.ui.updateButton.setEnabled(True)
        self.ui.inactiveButton.setEnabled(True)
        self.id_socio = str(index.data(Qt.UserRole))

    def clickedUpdateSocio(self):
        self.dict_socio = Socio.get_socio_id(self.id_socio)
        self.socio_update = SocioUpdateWindow(
            self.dict_socio, self.main_window, self.ui.labelMsj
        )
        self.socio_update.show()

    def clickedDeleteSocio(self):
        self.msj = Socio.delete_socio(self.id_socio)
        if self.ui.checkBox.isChecked():
            self.msj = f"<div style='color:#FF0000'><strong>{self.msj}</strong></div>"
        else:
            self.msj = f"<div style='color:#008F39'><strong>{self.msj}.</strong></div>"
        self.ui.labelMsj.setText(self.msj)
        QtTest.QTest.qWait(800)

        self.main_window.onClickedConsultaSocio()


class AlumnoUpdateWindow(QtWidgets.QWidget):
    def __init__(self, data_alumno: dict, main_window: MainWindow, msj_label):
        QtWidgets.QWidget.__init__(self)
        self.msj_label = msj_label
        self.data_alumno = data_alumno
        self.main_window = main_window
        self.data_alumno_update = dict()
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

        self.set_list_grado_model(self.list_model_grado)
        self.set_list_turno_model(self.list_model_turno)
        self.set_list_division_model(self.list_model_division)
        self.set_filter_socio_model(self.list_model_socio, self.combo_box_socio)

        self.main_window.set_icon_button(
            self.ui.saveAlumno, "../assets/icons/feather/save.svg"
        )
        self.main_window.set_icon_button(
            self.ui.pushButton, "../assets/icons/feather/x.svg"
        )

        self.combo_box_socio.setCurrentText(self.data_alumno["socio"])
        self.ui.comboBoxDivision.setCurrentText(self.data_alumno["division"])
        self.ui.comboBoxTurno.setCurrentText(self.data_alumno["turno"])
        self.ui.comboBoxGrado.setCurrentText(str(self.data_alumno["grado"]))
        self.ui.lineEditNombreAlumno.setText(self.data_alumno["nombre"])
        self.ui.lineEditApellidoAlumno.setText(self.data_alumno["apellido"])
        self.ui.lineEditDNIAlumno.setText(str(self.data_alumno["dni"]))

    def clickedSaveAlumno(self):
        self.data_alumno_update["id"] = self.data_alumno["id"]
        self.data_alumno_update["dni"] = self.ui.lineEditDNIAlumno.text()
        self.data_alumno_update["nombre"] = self.ui.lineEditNombreAlumno.text()
        self.data_alumno_update["apellido"] = self.ui.lineEditApellidoAlumno.text()
        self.data_alumno_update["socio"] = self.combo_box_socio.currentText()
        self.data_alumno_update["grado"] = self.ui.comboBoxGrado.currentText()
        self.data_alumno_update["division"] = self.ui.comboBoxDivision.currentText()
        self.data_alumno_update["turno"] = self.ui.comboBoxTurno.currentText()
        self.msj = Alumno.update_alumno_id(self.data_alumno_update)
        self.msj = f"<div style='color:#008F39'><strong>{self.msj}.</strong></div>"

        self.msj_label.setText(self.msj)
        self.deleteLater()
        QtTest.QTest.qWait(800)
        self.main_window.onClickedConsultaAlumno()

    def clickedExitFormAlumno(self):
        self.deleteLater()


class SocioUpdateWindow(QtWidgets.QWidget):
    def __init__(self, data_socio: dict, main_window: MainWindow, msj_label):
        QtWidgets.QWidget.__init__(self)
        self.data_socio = data_socio
        self.main_window = main_window
        self.msj_label = msj_label
        self.data_socio_update = dict()
        self.ui = Ui_FormSocio()
        self.setup()

    def setup(self):
        self.ui.setupUi(self)

        self.main_window.set_icon_button(
            self.ui.saveSocio, "../assets/icons/feather/save.svg"
        )
        self.main_window.set_icon_button(
            self.ui.botonSalir, "../assets/icons/feather/x.svg"
        )

        self.ui.lineEditDNISocio.setText(str(self.data_socio["dni"]))
        self.ui.lineEditNombreSocio.setText(self.data_socio["nombre"])
        self.ui.lineEditApellidoSocio.setText(self.data_socio["apellido"])
        self.ui.lineEditTelSocio.setText(str(self.data_socio["telefono"]))
        self.ui.lineEditDomicilioSocio.setText(self.data_socio["domicilio"])

    def clickedSaveSocio(self):
        self.data_socio_update["id"] = self.data_socio["id"]
        self.data_socio_update["dni"] = self.ui.lineEditDNISocio.text()
        self.data_socio_update["nombre"] = self.ui.lineEditNombreSocio.text()
        self.data_socio_update["apellido"] = self.ui.lineEditApellidoSocio.text()
        self.data_socio_update["telefono"] = self.ui.lineEditTelSocio.text()
        self.data_socio_update["domicilio"] = self.ui.lineEditDomicilioSocio.text()

        self.msj = Socio.update_socio_id(self.data_socio_update)
        self.msj = f"<div style='color:#008F39'><strong>{self.msj}.</strong></div>"

        self.msj_label.setText(self.msj)
        self.deleteLater()
        QtTest.QTest.qWait(800)
        self.main_window.onClickedConsultaSocio()

    def clickedExitFormSocio(self):
        self.deleteLater()
