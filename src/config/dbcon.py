import mongoengine
from config.env import *


class DB:
    def conectar(self):
        mongoengine.connect(alias=ALIAS, db=DB_NAME, host=HOST + DB_NAME)
