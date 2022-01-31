from datetime import date

import mongoengine
from PyQt5.QtCore import QThread, pyqtSignal


class Cobranza(mongoengine.Document):
<<<<<<< Updated upstream
=======
    nroDocumento = mongoengine.SequenceField()
>>>>>>> Stashed changes
    socio = mongoengine.ReferenceField("Socio")
    alumno = mongoengine.ReferenceField("Alumno")
    formaPago = mongoengine.StringField(required=True, max_length=25)
    fechaCobranza = mongoengine.DateField(required=True)
    mes = mongoengine.StringField(required=True, max_length=15)
    monto = mongoengine.FloatField(required=True, max_length=11)
    isAnulada = mongoengine.BooleanField(default=False)
    fechaCobranzaAnulada = mongoengine.DateField(required=False)
    descripcionCobranzaAnulada = mongoengine.StringField(required=False, max_length=100)


class CobranzaThreadSave(QThread):
    statusSaveCobranza = pyqtSignal((str,))

    def __init__(self):
        QThread.__init__(self)
        self.data_cobranza = None

    def check_cobranza_data(self, data_cobranza: dict):
        self.data_cobranza = data_cobranza

    def check_dict_cobranza(self, data_cobranza: dict):
        dict_check = True
        for value in data_cobranza.values():
            if value == "":
                dict_check = False
        return dict_check

    def get_len_cobranza_query(self, data_cobranza: dict):
        return len(
            Cobranza.objects(
                socio=data_cobranza["socio"],
                alumno=data_cobranza["alumno"],
                mes=data_cobranza["mes"],
                isAnulada=False,
            )
        )

    def run(self):
        # Guardamos cobranza
        if self.check_dict_cobranza(self.data_cobranza):
            self.today = date.today()
            try:
                if self.get_len_cobranza_query(self.data_cobranza):
                    self.statusSaveCobranza.emit("Cobranza Existente.")
                else:
                    obj_cobranza = Cobranza(
                        socio=self.data_cobranza["socio"],
                        alumno=self.data_cobranza["alumno"],
                        formaPago=self.data_cobranza["forma_pago"],
                        fechaCobranza=self.today,
                        mes=self.data_cobranza["mes"],
                        monto=self.data_cobranza["monto"],
                    )
                    obj_cobranza.save()

                    self.statusSaveCobranza.emit("")
            except:
                self.statusSaveCobranza.emit("Datos Incorrectos o incompletos.")
        else:
            self.statusSaveCobranza.emit("Datos Incorrectos o incompletos.")
