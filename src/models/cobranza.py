from datetime import date, datetime, timedelta

import mongoengine
import PyQt5
from dateutil.relativedelta import relativedelta
from models.socio import Alumno
from mongoengine import Q
from PyQt5.QtCore import QThread, pyqtSignal


class Cobranza(mongoengine.Document):
    nroDocumento = mongoengine.SequenceField()
    socio = mongoengine.ReferenceField("Socio")
    alumno = mongoengine.ReferenceField("Alumno")
    formaPago = mongoengine.StringField(required=True, max_length=25)
    fechaCobranza = mongoengine.DateField(required=True)
    periodo = mongoengine.StringField(required=True, max_length=6)
    monto = mongoengine.FloatField(required=True, max_length=11)
    isAnulada = mongoengine.BooleanField(default=False)
    fechaCobranzaAnulada = mongoengine.DateField(required=False)
    descripcionCobranzaAnulada = mongoengine.StringField(required=False, max_length=100)

    meta = {
        "collection": "cobranzas",
        "indexes": [{"fields": ["$nroDocumento", "$alumno", "$fechaCobranza"]}],
    }

    @classmethod
    def get_all_cobranzas(cls):
        fecha_desde = date.today() - relativedelta(months=1)
        fecha_hasta = date.today()

        filter = (
            Q(fechaCobranza__gte=fecha_desde) & Q(fechaCobranza__lte=fecha_hasta)
        ) & Q(isAnulada__icontains=False)
        cobranzas = cls.objects.filter(filter)

        array_cobranza = list()
        for cobranza in cobranzas:
            array_cobranza.append(cobranza)

        return array_cobranza

    @classmethod
    def get_all_cobranzas_anuladas(cls):
        fecha_desde = datetime.today() - relativedelta(months=1)
        fecha_hasta = datetime.today()

        filter = (
            Q(fechaCobranza__gte=fecha_desde) & Q(fechaCobranza__lte=fecha_hasta)
        ) & Q(isAnulada__icontains=True)
        cobranzas = cls.objects.filter(filter)
        array_cobranza = list()
        for cobranza in cobranzas:
            array_cobranza.append(cobranza)

        return array_cobranza

    @classmethod
    def get_cobranza_id(cls, id_cobranza: id):
        data_cobranza = cls.objects(id=id_cobranza).get()

        return data_cobranza

    @classmethod
    def anular_cobranza(cls, data_cobranza: dict):
        try:
            if data_cobranza["observacion"]:
                obj_cobranza = cls.objects(id=data_cobranza["id"]).get()
                obj_cobranza.update(
                    isAnulada=True,
                    fechaCobranzaAnulada=data_cobranza["fecha"],
                    descripcionCobranzaAnulada=data_cobranza["observacion"],
                )
                return ""
            else:
                return "Complete observación."

        except:
            return "Error al anular cobranza."

    @classmethod
    def get_search_cobranzas(cls, data_cobranza: dict):
        cobranzas_alumnos = []
        cobranzas = []

        if data_cobranza["fecha_desde"] > data_cobranza["fecha_hasta"]:
            return []

        if len(data_cobranza["search_str"]):
            filters = (
                Q(nombre__icontains=data_cobranza["search_str"])
                | Q(apellido__icontains=data_cobranza["search_str"])
            ) & Q(activo__icontains=True)
            alumnos = Alumno.objects.filter(filters)

            if len(alumnos) == 0:
                filters = Q(isAnulada__icontains=data_cobranza["anulada"]) & Q(formaPago__icontains=data_cobranza["search_str"])
                cobranzas = cls.objects.filter(filters)

                if len(cobranzas) == 0:

                    try:
                        cobranzas = cls.objects.filter(
                            Q(
                                __raw__={
                                    "$where": "this.nroDocumento.toString().match({})".format(
                                        int(data_cobranza["search_str"])
                                    )
                                }
                            )
                            & Q(isAnulada__icontains=data_cobranza["anulada"])

                        )
                    except ValueError:
                        cobranzas = []

                if len(cobranzas) == 0:
                    filters = Q(isAnulada__icontains=data_cobranza["anulada"]) & Q(periodo__icontains=data_cobranza["search_str"])

                    cobranzas = cls.objects.filter(filters)

                return cobranzas

            elif len(alumnos):
                for alumno in alumnos:
                    filters = (
                        Q(alumno__icontains=alumno.id)
                        & Q(isAnulada__icontains=data_cobranza["anulada"])
                    ) & (
                        Q(fechaCobranza__gte=data_cobranza["fecha_desde"])
                        & Q(fechaCobranza__lte=data_cobranza["fecha_hasta"])
                    )
                    cobranza = cls.objects.filter(filters)

                    if len(cobranza):
                        cobranzas_alumnos.append(cobranza)

                return cobranzas_alumnos if len(alumnos) > 1 else cobranza

            else:
                return []
        else:
            filters = (
                Q(fechaCobranza__gte=data_cobranza["fecha_desde"])
                & Q(fechaCobranza__lte=data_cobranza["fecha_hasta"])
            ) & Q(isAnulada__icontains=data_cobranza["anulada"])
            return cls.objects.filter(filters)


class CobranzaThreadSave(QThread):
    statusSaveCobranza = pyqtSignal((str,))

    def __init__(self):
        QThread.__init__(self)
        self.data_cobranza = None
        self.get_msj_check = None

    def check_cobranza_data(self, data_cobranza: dict):
        self.data_cobranza = data_cobranza

    def check_dict_cobranza(self, data_cobranza: dict):
        dict_check = True
        for value in data_cobranza.values():
            if value == "":
                dict_check = False
        return dict_check

    def check_cobranza_exist(self, data_cobranza: dict):
        return len(
            Cobranza.objects(
                alumno=data_cobranza["alumno"],
                periodo=data_cobranza["periodo"],
                isAnulada=False,
            )
        )

    def validate_cobranza_periodo(self, data_cobranza: dict):
        cobranzas = list()
        filters = Q(alumno__icontains=data_cobranza["alumno"]) & Q(
            isAnulada__icontains=False
        )
        data_cobranza_check = Cobranza.objects.filter(filters)
        if len(data_cobranza_check):
            for cobranza in data_cobranza_check:
                cobranzas.append(cobranza)

            year_insert_user = data_cobranza["periodo"][:4]
            month_insert_user = data_cobranza["periodo"][4:6]

            last_periodo = cobranzas.pop().periodo

            last_year = last_periodo[:4]
            next_month = int(last_periodo[4:6]) + 1

            if year_insert_user > last_year:
                return "{} {}".format("Complete las cobranzas del año:", last_year)

            if next_month > 12 and year_insert_user == last_year:
                return "{} {} {}".format("Periodos del año", last_year, "completado.")

            next_month = (
                str(next_month)
                if len(str(next_month)) != 1
                else "{}{}".format("0", str(next_month))
            )

            if year_insert_user == last_year and next_month != month_insert_user:
                return "{} {} {} {}/{}.".format(
                    "El próximo periodo del año", last_year, "es", last_year, next_month
                )
        else:
            year_insert_user = data_cobranza["periodo"][:4]
            month_insert_user = data_cobranza["periodo"][4:6]
            print(year_insert_user == str(date.today().year))
            if month_insert_user != '01' or year_insert_user != str(date.today().year):
                return "No existen cobranzas previas, ingrese periodo correcto."

        return ""

    def run(self):
        # Guardamos cobranza

        self.get_msj_check = self.validate_cobranza_periodo(
            self.data_cobranza
        )

        if self.check_dict_cobranza(self.data_cobranza):
            if self.check_cobranza_exist(self.data_cobranza):
                self.statusSaveCobranza.emit("Cobranza Existente.")

            elif self.get_msj_check != '':
                self.statusSaveCobranza.emit(self.get_msj_check)
            else:
                obj_cobranza = Cobranza(
                    socio=self.data_cobranza["socio"],
                    alumno=self.data_cobranza["alumno"],
                    formaPago=self.data_cobranza["forma_pago"],
                    fechaCobranza=self.data_cobranza["fecha"],
                    periodo=self.data_cobranza["periodo"],
                    monto=self.data_cobranza["monto"]
                )
                obj_cobranza.save()

                self.statusSaveCobranza.emit("")
        else:
            self.statusSaveCobranza.emit("Datos Incorrectos o incompletos.")
