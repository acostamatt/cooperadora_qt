# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/form_window_default.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormDefault(object):
    def setupUi(self, FormDefault):
        FormDefault.setObjectName("FormDefault")
        FormDefault.resize(464, 320)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FormDefault)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(FormDefault)
        QtCore.QMetaObject.connectSlotsByName(FormDefault)

    def retranslateUi(self, FormDefault):
        _translate = QtCore.QCoreApplication.translate
        FormDefault.setWindowTitle(_translate("FormDefault", "Form"))
