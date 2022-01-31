from models.socio import Alumno, Socio
from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from views.alumno.combo_box_extend import ExtendedComboBox


class ListSocioModel:
    def insert_data(self, modelComboBox: ExtendedComboBox):
        self.list_socio = Socio.get_all_socios_name()
        for socio in self.list_socio:
            modelComboBox.addItem(socio["socio"], socio["id"])


class ListAlumnoModel:
    def insert_data(self, modelComboBox: ExtendedComboBox, idSocio=None):
        if idSocio:
            self.list_alumno = Alumno.get_all_alumnos_name_by_socio(idSocio)
        else:
            self.list_alumno = Alumno.get_all_alumnos_name()

        for alumno in self.list_alumno:
            modelComboBox.addItem(alumno["alumno"], alumno["id"])


class ListGradoModel(QAbstractListModel):
    def __init__(self):
        QAbstractListModel.__init__(self)
        self.list_grado = [1, 2, 3, 4, 5, 6, 7]

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
        self.list_turno = ["Mañana", "Tarde"]

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
        self.list_division = ["A", "B", "C", "D", "E"]

    def rowCount(self, parent=None):
        return len(self.list_division)

    def data(self, index: QModelIndex, role=None):
        division = self.list_division[index.row()]
        if role == Qt.DisplayRole:
            return division

        if role == Qt.UserRole:
            return index.row()
