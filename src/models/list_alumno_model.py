from PyQt5 import QtCore

class ListGradoModel(QtCore.QAbstractListModel):
    def __init__(self):
        QtCore.QAbstractListModel.__init__(self)
        self.list_grado = [1,2,3,4,5,6,7]

    def rowCount(self, parent=None):
        return len(self.list_grado)

    def data(self, index: QtCore.QModelIndex, role=None):
        grado = self.list_grado[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return grado

        if role == QtCore.Qt.UserRole:
            return index.row()


class ListTurnoModel(QtCore.QAbstractListModel):
    def __init__(self):
        QtCore.QAbstractListModel.__init__(self)
        self.list_turno = ['Mañana','Tarde']


    def rowCount(self, parent=None):
        return len(self.list_turno)

    def data(self, index: QtCore.QModelIndex, role=None):
        turno = self.list_turno[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return turno

        if role == QtCore.Qt.UserRole:
            return index.row()


class ListDivisionModel(QtCore.QAbstractListModel):
    def __init__(self):
        QtCore.QAbstractListModel.__init__(self)
        self.list_division = ['A','B','C','D','E']

    def rowCount(self, parent=None):
        return len(self.list_division)

    def data(self, index: QtCore.QModelIndex, role=None):
        division = self.list_division[index.row()]
        if role == QtCore.Qt.DisplayRole:
            return division

        if role == QtCore.Qt.UserRole:
            return index.row()