from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt


class ListGradoModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)
        self.list_grado = [1,2,3,4,5,6,7]

    def rowCount(self, parent=None):
        return len(self.list_grado)

    def data(self, index: QModelIndex, role=None):
        grado = self.list_grado[index.row()]
        if role == Qt.DisplayRole:
            return grado

        if role == Qt.UserRole:
            return index.row()


class ListTurnoModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)
        self.list_turno = ['Mañana','Tarde']


    def rowCount(self, parent=None):
        return len(self.list_turno)

    def data(self, index: QModelIndex, role=None):
        turno = self.list_turno[index.row()]
        if role == Qt.DisplayRole:
            return turno

        if role == Qt.UserRole:
            return index.row()


class ListDivisionModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)
        self.list_division = ['A','B','C','D','E']

    def rowCount(self, parent=None):
        return len(self.list_division)

    def data(self, index: QModelIndex, role=None):
        division = self.list_division[index.row()]
        if role == Qt.DisplayRole:
            return division

        if role == Qt.UserRole:
            return index.row()