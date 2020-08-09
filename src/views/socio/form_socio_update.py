# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/form_socio_update.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormSocioUpdate(object):
    def setupUi(self, FormSocioUpdate):
        FormSocioUpdate.setObjectName("FormSocioUpdate")
        FormSocioUpdate.resize(212, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(FormSocioUpdate.sizePolicy().hasHeightForWidth())
        FormSocioUpdate.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(FormSocioUpdate)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditDNISocio = QtWidgets.QLineEdit(FormSocioUpdate)
        self.lineEditDNISocio.setObjectName("lineEditDNISocio")
        self.verticalLayout.addWidget(self.lineEditDNISocio)
        self.lineEditApellidoSocio = QtWidgets.QLineEdit(FormSocioUpdate)
        self.lineEditApellidoSocio.setText("")
        self.lineEditApellidoSocio.setObjectName("lineEditApellidoSocio")
        self.verticalLayout.addWidget(self.lineEditApellidoSocio)
        self.lineEditNombreSocio = QtWidgets.QLineEdit(FormSocioUpdate)
        self.lineEditNombreSocio.setObjectName("lineEditNombreSocio")
        self.verticalLayout.addWidget(self.lineEditNombreSocio)
        self.lineEditDomicilioSocio = QtWidgets.QLineEdit(FormSocioUpdate)
        self.lineEditDomicilioSocio.setObjectName("lineEditDomicilioSocio")
        self.verticalLayout.addWidget(self.lineEditDomicilioSocio)
        self.lineEditTelSocio = QtWidgets.QLineEdit(FormSocioUpdate)
        self.lineEditTelSocio.setObjectName("lineEditTelSocio")
        self.verticalLayout.addWidget(self.lineEditTelSocio)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botonSalir = QtWidgets.QPushButton(FormSocioUpdate)
        self.botonSalir.setEnabled(True)
        self.botonSalir.setObjectName("botonSalir")
        self.horizontalLayout.addWidget(self.botonSalir)
        self.botonAgregarOtroAlumno = QtWidgets.QPushButton(FormSocioUpdate)
        self.botonAgregarOtroAlumno.setEnabled(True)
        self.botonAgregarOtroAlumno.setObjectName("botonAgregarOtroAlumno")
        self.horizontalLayout.addWidget(self.botonAgregarOtroAlumno)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(FormSocioUpdate)
        self.botonSalir.clicked.connect(FormSocioUpdate.clickedExitFormSocio)
        self.botonAgregarOtroAlumno.clicked.connect(FormSocioUpdate.clickedUpdateSocio)
        self.botonSalir.clicked.connect(FormSocioUpdate.clickedExitFormSocio)
        QtCore.QMetaObject.connectSlotsByName(FormSocioUpdate)

    def retranslateUi(self, FormSocioUpdate):
        _translate = QtCore.QCoreApplication.translate
        FormSocioUpdate.setWindowTitle(_translate("FormSocioUpdate", "Formulario Socio"))
        self.lineEditDNISocio.setPlaceholderText(_translate("FormSocioUpdate", "D.N.I"))
        self.lineEditApellidoSocio.setPlaceholderText(_translate("FormSocioUpdate", "Apellido"))
        self.lineEditNombreSocio.setPlaceholderText(_translate("FormSocioUpdate", "Nombre"))
        self.lineEditDomicilioSocio.setPlaceholderText(_translate("FormSocioUpdate", "Domicilio"))
        self.lineEditTelSocio.setPlaceholderText(_translate("FormSocioUpdate", "Teléfono"))
        self.botonSalir.setText(_translate("FormSocioUpdate", "Salir"))
        self.botonAgregarOtroAlumno.setText(_translate("FormSocioUpdate", "Actualizar"))
