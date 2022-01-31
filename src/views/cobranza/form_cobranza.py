from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QPushButton

from models.combo_box_extend import ExtendedComboBox
from models.list_alumno_model import ListAlumnoModel, ListSocioModel
from models.list_forma_pago_model import ListFormaPagoModel
from models.list_mes_model import ListMesModel
from views.base.form_cobranza_base import Ui_FormCobranza


class FormCobranza(QtWidgets.QWidget):
    saveCobranzaData = pyqtSignal((dict,))

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_FormCobranza()
        self.setup()

    def set_filter_socio_model(
        self, model: ListSocioModel, combo_box_extend: ExtendedComboBox
    ):
        model.insert_data(combo_box_extend)
        self.ui.horizontalLayout_3.addWidget(combo_box_extend)

    def set_filter_alumno_model(
        self, model: ListAlumnoModel, combo_box_extend: ExtendedComboBox, idSocio=None
    ):
        if idSocio:
            model.insert_data(combo_box_extend, idSocio)

        self.ui.horizontalLayout_2.addWidget(combo_box_extend)

    def set_list_forma_pago(self, model):
        self.ui.comboBoxFormaPago.setModel(model)

    def set_list_mes(self, model):
        self.ui.comboBoxMes.setModel(model)

    def setup(self):
        self.ui.setupUi(self)

        self.combo_box_socio = ExtendedComboBox()
        self.combo_box_alumno = ExtendedComboBox()
        self.list_model_socio = ListSocioModel()
        self.list_model_alumno = ListAlumnoModel()

        self.list_model_forma_pago = ListFormaPagoModel()
        self.list_model_mes = ListMesModel()

        self.set_icon_button(self.ui.saveCobranza, "../assets/icons/feather/save.svg")
        self.set_icon_button(self.ui.salir, "../assets/icons/feather/x.svg")

        self.set_filter_socio_model(self.list_model_socio, self.combo_box_socio)
        self.set_filter_alumno_model(self.list_model_alumno, self.combo_box_alumno)
        self.set_list_forma_pago(self.list_model_forma_pago)
        self.set_list_mes(self.list_model_mes)

        self.combo_box_socio.setCurrentIndex(-1)
        self.combo_box_alumno.setCurrentIndex(-1)
        self.ui.comboBoxFormaPago.setCurrentIndex(-1)
        self.ui.comboBoxMes.setCurrentIndex(-1)
        self.combo_box_socio.currentIndexChanged.connect(self.changeSocioSelected)

    def clickedSaveCobranza(self):
        self.dict_cobranza = dict()
        self.dict_cobranza["socio"] = self.combo_box_socio.currentData(Qt.UserRole)
        self.dict_cobranza["alumno"] = self.combo_box_alumno.currentData(Qt.UserRole)
        self.dict_cobranza["forma_pago"] = self.ui.comboBoxFormaPago.currentData(
            Qt.UserRole
        )
        self.dict_cobranza["mes"] = self.ui.comboBoxMes.currentData(Qt.UserRole)
        self.dict_cobranza["monto"] = self.ui.lineEditMontoCobranza.text()

        self.saveCobranzaData.emit(self.dict_cobranza)

    def clickedExitFormCobranza(self):
        self.ui.labelMsjCobranza.setText("")
        self.deleteLater()

    def changeSocioSelected(self):
        self.combo_box_alumno.clear()
        self.set_filter_alumno_model(
            self.list_model_alumno,
            self.combo_box_alumno,
            self.combo_box_socio.currentData(Qt.UserRole),
        )
        self.combo_box_alumno.setCurrentIndex(-1)

    def set_msj_save_cobranza(self, msj):
        if msj == "":
            self.clean_data_cobranza()

            mensaje_exito = "<div style='color:#008F39'><strong>Datos guardados correctamente.</strong></div>"
            self.ui.labelMsjCobranza.setText("")
            self.ui.labelMsjCobranza.setText(mensaje_exito)
        else:
            mensaje_error = f"<div style='color:#FF0000'><strong>{msj}</strong></div>"
            self.ui.labelMsjCobranza.setText("")
            self.ui.labelMsjCobranza.setText(mensaje_error)

    def set_data_cobranza(self, data_cobranza: dict):
        self.combo_box_socio.setCurrentIndex(data_cobranza["socio"])
        self.combo_box_alumno.setCurrentIndex(data_cobranza["alumno"])
        self.ui.comboBoxFormaPago.setCurrentIndex(data_cobranza["forma_pago"])
        self.ui.comboBoxMes.setCurrentIndex(str(data_cobranza["mes"]))
        self.ui.lineEditMontoCobranza.setText(str(data_cobranza["monto"]))

    def set_icon_button(self, buttonIcon: QPushButton, urlIcon):
        buttonIcon.setIcon(QtGui.QIcon(urlIcon))
        buttonIcon.setIconSize(QtCore.QSize(20, 20))
        buttonIcon.setGeometry(QtCore.QRect(1030, 500, 161, 61))

    def clean_data_cobranza(self):
        self.combo_box_socio.setCurrentIndex(-1)
        self.combo_box_alumno.setCurrentIndex(-1)
        self.ui.comboBoxFormaPago.setCurrentIndex(-1)
        self.ui.comboBoxMes.setCurrentIndex(-1)
        self.ui.lineEditMontoCobranza.setText("")

    def cleanLayout(self, layout):
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()
