from PyQt5.QtCore import QObject

from controllers.form_alumno import FormAlumnoController
from controllers.form_cobranza import FormCobranzaController
from controllers.form_socio import FormSocioController
from views.alumno.form_alumno import FormAlumno
from views.cobranza.form_cobranza import FormCobranza
from views.main_window.main_window import MainWindow
from views.socio.form_socio import FormSocio


class MainWindowController(QObject):
    def __init__(self, main: MainWindow):
        QObject.__init__(self)
        self.__main = main
        self.__main.clickedNewSocio.connect(self.__onclickedNewSocio)
        self.__main.clickedNewAlumno.connect(self.__onclickedNewAlumno)
        self.__main.clickedNewCobranza.connect(self.__onclickedNewCobranza)

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

    def __onclickedNewCobranza(self):
        self.__cobranza = FormCobranza()
        self.__cobranza_controller = FormCobranzaController(self.__cobranza)
        self.__cobranza_controller.show_view()
