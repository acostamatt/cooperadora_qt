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
