from PyQt5.QtCore import QObject

from controllers.form_socio import FormSocioController
from controllers.form_alumno import FormAlumnoController
from views.socio.form_socio import FormSocio
from views.alumno.form_alumno import FormAlumno
from views.main_window.main_window import MainWindow

class MainWindowController(QObject):
    def __init__(self, main: MainWindow):
        QObject.__init__(self)
        self.__main = main
        self.__main.clickedNewSocio.connect(self.__onclickedNewSocio)
        self.__main.clickedNewAlumno.connect(self.__onclickedNewAlumno)

    def show_view(self):
        self.__main.show()

    def __onclickedNewSocio(self):
        self.__socio = FormSocio()
        self.__socio_controller = FormSocioController(self.__socio)
        self.__socio_controller.show_view()

    def __onclickedNewAlumno(self):
        self.__alumno = FormAlumno()
        self.__alumno_controller = FormAlumnoController(self.__alumno)
        self.__alumno_controller.show_view()