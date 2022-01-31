from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt


class ListMesModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)
        self.list_mes = [
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre",
        ]

    def rowCount(self, parent=None):
        return len(self.list_mes)

    def data(self, index: QModelIndex, role=None):
        mes = self.list_mes[index.row()]
        if role == Qt.DisplayRole:
            return mes

        if role == Qt.UserRole:
            return index.row()
