# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.vboxlayout = QtWidgets.QVBoxLayout(Form)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label_img_user = QtWidgets.QLabel(Form)
        self.label_img_user.setStyleSheet("image: url(:/assets/icons/feather/user.svg);")
        self.label_img_user.setText("")
        self.label_img_user.setObjectName("label_img_user")
        self.vboxlayout.addWidget(self.label_img_user)
        self.line_edit_user = QtWidgets.QLineEdit(Form)
        self.line_edit_user.setObjectName("line_edit_user")
        self.vboxlayout.addWidget(self.line_edit_user)
        self.line_edit_pass = QtWidgets.QLineEdit(Form)
        self.line_edit_pass.setObjectName("line_edit_pass")
        self.vboxlayout.addWidget(self.line_edit_pass)
        self.boton_check = QtWidgets.QPushButton(Form)
        self.boton_check.setObjectName("boton_check")
        self.vboxlayout.addWidget(self.boton_check)
        self.check_view_pass = QtWidgets.QCheckBox(Form)
        self.check_view_pass.setObjectName("check_view_pass")
        self.vboxlayout.addWidget(self.check_view_pass)
        self.label_msj = QtWidgets.QLabel(Form)
        self.label_msj.setEnabled(True)
        self.label_msj.setText("")
        self.label_msj.setObjectName("label_msj")
        self.vboxlayout.addWidget(self.label_msj)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Usuario"))
        self.line_edit_user.setPlaceholderText(_translate("Form", "Introduzca Usuario"))
        self.line_edit_pass.setPlaceholderText(_translate("Form", "Contraseña"))
        self.boton_check.setText(_translate("Form", "Ingresar"))
        self.check_view_pass.setText(_translate("Form", "Mostrar contraseña"))
import resources
