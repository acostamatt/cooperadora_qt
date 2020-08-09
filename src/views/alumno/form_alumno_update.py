# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/form_alumno_update.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormAlumnoUpdate(object):
    def setupUi(self, FormAlumnoUpdate):
        FormAlumnoUpdate.setObjectName("FormAlumnoUpdate")
        FormAlumnoUpdate.resize(250, 322)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormAlumnoUpdate.sizePolicy().hasHeightForWidth())
        FormAlumnoUpdate.setSizePolicy(sizePolicy)
        FormAlumnoUpdate.setMaximumSize(QtCore.QSize(250, 322))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(FormAlumnoUpdate)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditDNIAlumno = QtWidgets.QLineEdit(FormAlumnoUpdate)
        self.lineEditDNIAlumno.setObjectName("lineEditDNIAlumno")
        self.verticalLayout_2.addWidget(self.lineEditDNIAlumno)
        self.lineEditApellidoAlumno = QtWidgets.QLineEdit(FormAlumnoUpdate)
        self.lineEditApellidoAlumno.setText("")
        self.lineEditApellidoAlumno.setObjectName("lineEditApellidoAlumno")
        self.verticalLayout_2.addWidget(self.lineEditApellidoAlumno)
        self.lineEditNombreAlumno = QtWidgets.QLineEdit(FormAlumnoUpdate)
        self.lineEditNombreAlumno.setObjectName("lineEditNombreAlumno")
        self.verticalLayout_2.addWidget(self.lineEditNombreAlumno)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelGrado = QtWidgets.QLabel(FormAlumnoUpdate)
        self.labelGrado.setObjectName("labelGrado")
        self.horizontalLayout_2.addWidget(self.labelGrado)
        self.comboBoxGrado = QtWidgets.QComboBox(FormAlumnoUpdate)
        self.comboBoxGrado.setObjectName("comboBoxGrado")
        self.horizontalLayout_2.addWidget(self.comboBoxGrado)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelDivision = QtWidgets.QLabel(FormAlumnoUpdate)
        self.labelDivision.setObjectName("labelDivision")
        self.horizontalLayout.addWidget(self.labelDivision)
        self.comboBoxDivision = QtWidgets.QComboBox(FormAlumnoUpdate)
        self.comboBoxDivision.setObjectName("comboBoxDivision")
        self.horizontalLayout.addWidget(self.comboBoxDivision)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelTurno = QtWidgets.QLabel(FormAlumnoUpdate)
        self.labelTurno.setObjectName("labelTurno")
        self.horizontalLayout_5.addWidget(self.labelTurno)
        self.comboBoxTurno = QtWidgets.QComboBox(FormAlumnoUpdate)
        self.comboBoxTurno.setObjectName("comboBoxTurno")
        self.horizontalLayout_5.addWidget(self.comboBoxTurno)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.updateAlumno = QtWidgets.QPushButton(FormAlumnoUpdate)
        self.updateAlumno.setObjectName("updateAlumno")
        self.verticalLayout_2.addWidget(self.updateAlumno)
        self.pushButton = QtWidgets.QPushButton(FormAlumnoUpdate)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(FormAlumnoUpdate)
        self.updateAlumno.clicked.connect(FormAlumnoUpdate.clickedUpdateAlumno)
        self.pushButton.clicked.connect(FormAlumnoUpdate.clickedExitFormAlumno)
        QtCore.QMetaObject.connectSlotsByName(FormAlumnoUpdate)

    def retranslateUi(self, FormAlumnoUpdate):
        _translate = QtCore.QCoreApplication.translate
        FormAlumnoUpdate.setWindowTitle(_translate("FormAlumnoUpdate", "Formulario Socio"))
        self.lineEditDNIAlumno.setPlaceholderText(_translate("FormAlumnoUpdate", "D.N.I"))
        self.lineEditApellidoAlumno.setPlaceholderText(_translate("FormAlumnoUpdate", "Apellido"))
        self.lineEditNombreAlumno.setPlaceholderText(_translate("FormAlumnoUpdate", "Nombre"))
        self.labelGrado.setText(_translate("FormAlumnoUpdate", "Grado"))
        self.labelDivision.setText(_translate("FormAlumnoUpdate", "División"))
        self.labelTurno.setText(_translate("FormAlumnoUpdate", "Turno"))
        self.updateAlumno.setText(_translate("FormAlumnoUpdate", "Actualizar"))
        self.pushButton.setText(_translate("FormAlumnoUpdate", "Salir"))
