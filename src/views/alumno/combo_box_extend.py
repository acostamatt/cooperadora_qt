from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtWidgets import QComboBox, QCompleter


class ExtendedComboBox(QComboBox):
    def __init__(self):
        QComboBox.__init__(self)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        self.filter_model = QSortFilterProxyModel(self)
        self.filter_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_model.setSourceModel(self.model())

        self.completer = QCompleter(self.filter_model, self)

        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        self.lineEdit().textEdited.connect(self.filter_model.setFilterFixedString)

        self.completer.activated.connect(self.on_completer_activated)

    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))

    def setModel(self, model):
        self.setModel(model)
        self.filter_model.setSourceModel(model)
        self.completer.setModel(self.filter_model)

    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.filter_model.setFilterKeyColumn(column)
        self.setModelColumn(column)
