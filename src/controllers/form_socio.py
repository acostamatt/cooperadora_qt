from models.socio import SocioThreadSave
from PyQt5.QtCore import QObject
from views.socio.form_socio import FormSocio


class FormSocioController(QObject):
    def __init__(self, form_socio: FormSocio):
        QObject.__init__(self)
        self.__socio_view = form_socio
        self.__socio_view_thread_save = SocioThreadSave()

        self.__socio_view.saveSocioData.connect(self.__on_save_socio)

        self.__socio_view_thread_save.statusSaveSocio.connect(
            self.__on_save_socio_checked
        )

    def cleanLayout(self, layout):
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()

    def __on_save_socio(self, dict_socio: dict):
        self.__socio_view_thread_save.start()
        self.__socio_view_thread_save.check_socio_data(dict_socio)

    def __on_save_socio_checked(self, msj):
        self.__socio_view.set_msj_save_socio(msj)

    def __on_msj_status_socio_exist(self, msj):
        self.__socio_view.set_msj_save_socio(msj)

    def __on_save_socio_exist(self, data_socio: dict):
        self.__socio_view.set_data_socio(data_socio)

    def check_thread_running(self, thread):
        if thread and thread.isRunning():
            thread.terminate()
            thread.wait()

    def show_view(self):
        self.__socio_view.show()
