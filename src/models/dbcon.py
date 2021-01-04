import mongoengine
class DB:
    def conectar(self):
        mongoengine.connect(alias="default", db='cooperadora', host='mongodb://localhost/cooperadora')
