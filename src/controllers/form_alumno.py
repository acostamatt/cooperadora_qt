from PyQt5.QtCore import QObject

from models.socio import AlumnoThreadSave
from views.alumno.form_alumno import FormAlumno


class FormAlumnoController(QObject):
    def __init__(self, form_alumno: FormAlumno):
        QObject.__init__(self)
        self.__alumno_view = form_alumno
        self.__alumno_view_thread_save = AlumnoThreadSave()

        self.__alumno_view.saveAlumnoData.connect(self.__on_save_alumno)

        self.__alumno_view_thread_save.statusSaveAlumno.connect(
            self.__on_save_alumno_checked
        )

    def cleanLayout(self, layout):
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater()

    def __on_save_alumno(self, dict_alumno: dict):
        self.__alumno_view_thread_save.start()
        self.__alumno_view_thread_save.check_alumno_data(dict_alumno)

    def __on_save_alumno_checked(self, msj):
        self.__alumno_view.set_msj_save_alumno(msj)

    def __on_msj_status_alumno_exist(self, msj):
        self.__alumno_view.set_msj_save_alumno(msj)

    def __on_save_socio_exist(self, data_alumno: dict):
        self.__alumno_view.set_data_socio(data_alumno)

    def check_thread_running(self, thread):
        if thread and thread.isRunning():
            thread.terminate()
            thread.wait()

    def show_view(self):
        self.__alumno_view.show()
