from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QSize
from models.socio import Socio

class SociosTableModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        self.headers = ["Socio", "DNI", "Cant. Alumnos", "Domicilio"]
        self.headers_widths = [1, 1, 1, 1]
        self.socios = []

    def rowCount(self, parent=None):
        return len(self.socios)

    def columnCount(self, parent=None):
        return len(self.headers)

    def refresh_data(self):
        self.socios = Socio.get_all_socios()
        self.modelReset.emit()

    def refresh_data_search(self, search_txt: str, check_socio):
        self.socios = Socio.get_search_socios(search_txt, check_socio)
        self.modelReset.emit()

    def data(self, index: QModelIndex, role=None):
        socio = self.socios[index.row()]

        if role == Qt.DisplayRole:
            if index.column() == 0:
                return socio.apellido+', '+socio.nombre

            if index.column() == 1:
                return socio.dni

            if index.column() == 2:
                return len(socio.alumnos)

            if index.column() == 3:
                return socio.domicilio

        if role == Qt.UserRole:
            return socio.id

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return self.headers[section]

            if role == Qt.SizeHintRole:
                return QSize(self.headers_widths[section], 23)  # 23, numero mágico (?