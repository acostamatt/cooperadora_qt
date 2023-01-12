from models.cobranza import Cobranza
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QSize, Qt


class CobranzasTableModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        self.headers = [
            "Alumno",
            "Socio",
            "Nro",
            "Periodo",
            "Fecha",
            "Forma Pago",
            "Monto",
        ]
        self.headers_widths = [200, 200, 100, 100, 200, 200, 100]
        self.cobranzas = []

    def refresh_data(self):
        self.cobranzas = Cobranza.get_all_cobranzas()
        self.modelReset.emit()

    def refresh_data_search(self, data_cobranza: dict):
        self.cobranzas = Cobranza.get_search_cobranzas(data_cobranza)
        self.modelReset.emit()

    def rowCount(self, parent=None):
        return len(self.cobranzas)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index: QModelIndex, role=None):
        cobranza = self.cobranzas[index.row()]

        if role == Qt.DisplayRole:

            if index.column() == 0:
                return f"{cobranza.alumno.apellido}, {cobranza.alumno.nombre}"

            if index.column() == 1:
                return f"{cobranza.socio.apellido}, {cobranza.socio.nombre}"

            if index.column() == 2:
                return cobranza.nroDocumento

            if index.column() == 3:
                return cobranza.periodo[:4] + "/" + cobranza.periodo[4:6]

            if index.column() == 4:
                return str(cobranza.fechaCobranza)

            if index.column() == 5:
                return cobranza.formaPago

            if index.column() == 6:
                return cobranza.monto

        if role == Qt.UserRole:
            return cobranza.id

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return self.headers[section]

        if role == Qt.SizeHintRole:
            return QSize(self.headers_widths[section], 23)
