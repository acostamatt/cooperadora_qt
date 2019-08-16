from PyQt5.QtCore import pyqtSignal, QObject

from models.login import LoginModel


class LoginDao(QObject):
    db = None

    def __init__(self, db):
        QObject.__init__(self)
        self.db = db
        self.db.conectar("localhost","root","","cooperadora")


    def comprobar_usuario(self, login: LoginModel):
        with self.db.connection.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE usuario = %s AND pass = %s"
            cursor.execute(sql, (login.user, login.passw,))
            return cursor.fetchall()