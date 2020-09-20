from PyQt5 import QtCore

from models.socio import Alumno


class AlumnosTableModel(QtCore.QAbstractTableModel):
    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self)
        self.headers = ["Alumno", "Grado", "Division", "Turno", "Socio"]
        self.headers_widths = [200, 200, 200, 200, 200]
        self.alumnos = Alumno.obtener_alumnos()

    def refresh_data(self):
        # self.alumnos = Alumno.obtener_alumnos()
        self.modelReset.emit()

    def rowCount(self, parent=None):
        return len(self.alumnos)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index: QtCore.QModelIndex, role=None):
        alumno = self.alumnos[index.row()]
        socio = Alumno.obtener_socio_por_alumno(alumno.id)
        if role == QtCore.Qt.DisplayRole:
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

        if role == QtCore.Qt.UserRole:
            return alumno.id

    def headerData(self, section, orientation, role=None):
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.DisplayRole:
                return self.headers[section]

            if role == QtCore.Qt.SizeHintRole:
                return QtCore.QSize(self.headers_widths[section], 23)