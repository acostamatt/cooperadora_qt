import pymysql

class DB:
    connection = None
    def conectar(self, host, usuario, password, db, charset='utf8'):
        self.connection = pymysql.connect(host=host,
                                          user=usuario,
                                          password=password,
                                          db=db,
                                          charset=charset,
                                          cursorclass=pymysql.cursors.DictCursor)
