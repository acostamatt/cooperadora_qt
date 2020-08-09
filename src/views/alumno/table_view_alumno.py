# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/table_view_alumno.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableAlumno(object):
    def setupUi(self, TableAlumno):
        TableAlumno.setObjectName("TableAlumno")
        TableAlumno.resize(612, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(TableAlumno)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(TableAlumno)
        self.tableView.setMinimumSize(QtCore.QSize(600, 0))
        self.tableView.setStyleSheet("")
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.labelMsj = QtWidgets.QLabel(TableAlumno)
        self.labelMsj.setText("")
        self.labelMsj.setObjectName("labelMsj")
        self.horizontalLayout_2.addWidget(self.labelMsj)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.updateButton = QtWidgets.QPushButton(TableAlumno)
        self.updateButton.setEnabled(False)
        self.updateButton.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.updateButton)
        self.deleteButton = QtWidgets.QPushButton(TableAlumno)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TableAlumno)
        self.updateButton.clicked.connect(TableAlumno.clickedUpdateAlumno)
        self.deleteButton.clicked.connect(TableAlumno.clickedDeleteAlumno)
        QtCore.QMetaObject.connectSlotsByName(TableAlumno)

    def retranslateUi(self, TableAlumno):
        _translate = QtCore.QCoreApplication.translate
        TableAlumno.setWindowTitle(_translate("TableAlumno", "Form"))
        self.updateButton.setText(_translate("TableAlumno", "Actualizar"))
        self.deleteButton.setText(_translate("TableAlumno", "Eliminar"))
