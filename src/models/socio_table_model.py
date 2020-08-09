from PyQt5 import QtCore

from models.socio import Socio

class SociosTableModel(QtCore.QAbstractTableModel):
    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self)
        self.headers = ["Socio", "DNI", "Cant. Alumnos", "Domicilio"]
        self.headers_widths = [1, 1, 1, 1]
        self.socios = Socio.obtener_socios()

    def rowCount(self, parent=None):
        return len(self.socios)

    def columnCount(self, parent=None):
        return len(self.headers)

    def refresh_data(self):
        self.alumnos = Socio.obtener_socios()
        self.modelReset.emit()

    def data(self, index: QtCore.QModelIndex, role=None):
        socio = self.socios[index.row()]

        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return socio.apellido+', '+socio.nombre

            if index.column() == 1:
                return socio.dni

            if index.column() == 2:
                return len(socio.alumnos)

            if index.column() == 3:
                return socio.domicilio

        if role == QtCore.Qt.UserRole:
            return socio.id

    def headerData(self, section, orientation, role=None):
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.DisplayRole:
                return self.headers[section]

            if role == QtCore.Qt.SizeHintRole:
                return QtCore.QSize(self.headers_widths[section], 23)  # 23, numero mágico (?