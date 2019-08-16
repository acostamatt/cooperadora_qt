class LoginModel:
    def __init__(self, id=None, user=None, passw=None):
        self.id = id
        self.user = user
        self.passw = passw

    def validar(self):
        errores = []

        if not self.user:
            errores.append("Falta usuario")

        if not self.passw:
            errores.append("Falta contraseña")

        return errores