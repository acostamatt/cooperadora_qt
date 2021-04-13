import mongoengine
from PyQt5.QtCore import QThread, pyqtSignal


class Usuario(mongoengine.Document):
    usuario = mongoengine.StringField(required=True, max_length=50)
    passw = mongoengine.StringField(required=True, max_length=50)
    meta = {'collection':'usuarios'}

class UserThread(QThread):
    checkUser = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def check_user_data(self, user, passw):
        self.nombre_user = user
        self.pass_user = passw

    def run(self):
        try:
            Usuario.objects(usuario=self.nombre_user, passw=self.pass_user).get()
            self.checkUser.emit('')
        except Exception:
            self.checkUser.emit('Usuario y/o contraseña incorrecta.')


