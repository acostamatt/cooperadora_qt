from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt


class ListFormaPagoModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)
        self.list_forma_pago = ["Efectivo", "Cheque"]

    def rowCount(self, parent=None):
        return len(self.list_forma_pago)

    def data(self, index: QModelIndex, role=None):
        forma_pago = self.list_forma_pago[index.row()]
        if role == Qt.DisplayRole:
            return forma_pago

        if role == Qt.UserRole:
            return index.row()
