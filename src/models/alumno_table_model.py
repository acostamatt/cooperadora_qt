from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt, QModelIndex, QAbstractTableModel

from models.socio import Alumno


class AlumnosTableModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        self.headers = ["Alumno", "Grado", "Division", "Turno", "Socio"]
        self.headers_widths = [200, 200, 200, 200, 200]
        self.alumnos = []

    def refresh_data(self):
        self.alumnos = Alumno.get_all_alumnos()
        self.modelReset.emit()

    def refresh_data_search(self, search_txt: str, check_alumno: bool):
        self.alumnos = Alumno.get_search_alumnos(search_txt, check_alumno)
        self.modelReset.emit()

    def rowCount(self, parent=None):
        return len(self.alumnos)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index: QModelIndex, role=None):
        alumno = self.alumnos[index.row()]
        socio = Alumno.get_socio_by_alumno(alumno.id)
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return alumno.apellido+', '+alumno.nombre

            if index.column() == 1:
                return alumno.grado

            if index.column() == 2:
                return alumno.division

            if index.column() == 3:
                return alumno.turno

            if index.column() == 4:
                return socio

        if role == Qt.UserRole:
            return alumno.id

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return self.headers[section]

            if role == Qt.SizeHintRole:
                return QSize(self.headers_widths[section], 23)