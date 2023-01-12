from models.cobranza import CobranzaThreadSave
from PyQt5.QtCore import QObject
from views.cobranza.form_cobranza import FormCobranza


class FormCobranzaController(QObject):
    def __init__(self, form_cobranza: FormCobranza):
        QObject.__init__(self)
        self.__cobranza_view = form_cobranza
        self.__cobranza_view_thread_save = CobranzaThreadSave()

        self.__cobranza_view.saveCobranzaData.connect(self.__on_save_cobranza)

        self.__cobranza_view_thread_save.statusSaveCobranza.connect(
            self.__on_save_cobranza_checked
        )

    def cleanLayout(self, layout):
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()

    def __on_save_cobranza(self, dict_cobranza: dict):
        self.__cobranza_view_thread_save.start()
        self.__cobranza_view_thread_save.check_cobranza_data(dict_cobranza)

    def __on_save_cobranza_checked(self, msj):
        self.__cobranza_view.set_msj_save_cobranza(msj)

    def __on_msj_status_cobranza_exist(self, msj):
        self.__cobranza_view.set_msj_save_socio(msj)

    def __on_save_cobranza_exist(self, data_cobranza: dict):
        self.__cobranza_view.set_data_cobranza(data_cobranza)

    def check_thread_running(self, thread):
        if thread and thread.isRunning():
            thread.terminate()
            thread.wait()

    def show_view(self):
        self.__cobranza_view.show()
