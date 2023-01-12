import time

import bson
import mongoengine
from mongoengine.queryset.visitor import Q
class DB:
    def conectar(self):
        mongoengine.connect(alias="default", db='cooperadora', host='mongodb://localhost/cooperadora')
    def desconectar(self):
        mongoengine.disconnect(alias="default", db='cooperadora')

class Alumno(mongoengine.Document):
    nombre = mongoengine.StringField(required=True, max_length=50)
    apellido = mongoengine.StringField(required=True, max_length=50)
    grado = mongoengine.IntField(required=True, max_length=1)
    dni = mongoengine.IntField(required=True, max_length=8)
    turno = mongoengine.StringField(required=True, max_length=6)
    division = mongoengine.StringField(required=True, max_length=1)
    activo = mongoengine.BooleanField(required=True)
    ciclo = mongoengine.IntField(required=True, max_length=4)

    meta = {
        "collection": "alumnos",
        "indexes": [
            {"fields": ["$nombre", "$apellido", "$grado", "$turno", "$division"]}
        ],
    }

    @staticmethod
    def obtener_alumnos():
        alumnos = Alumno.objects
        array_alumno = list()
        for alumno in alumnos:
            array_alumno.append(alumno)

        return array_alumno

    @staticmethod
    def obtener_socio_alumno(id_alumno):
        for socio in Socio.objects:
            for list_socio in socio.alumnos:
                if str(id_alumno) == str(list_socio.id):
                    return socio.apellido+', '+socio.nombre

class Socio(mongoengine.Document):
    nombre = mongoengine.StringField(required=True, max_length=50)
    apellido = mongoengine.StringField(required=True, max_length=50)
    dni = mongoengine.IntField(required=True, max_length=8)
    domicilio = mongoengine.StringField(required=True, max_length=100)
    telefono = mongoengine.IntField(required=True, max_length=15)
    activo = mongoengine.BooleanField(required=True)
    alumnos = mongoengine.ListField(mongoengine.ReferenceField('Alumno', reverse_delete_rule=mongoengine.PULL))
    #meta = {'collection':'socios'}
    
    meta = {'collection':'socios', 
            'indexes': [{
                'fields': ['$nombre', "$apellido", "$dni", "$domicilio", "$telefono"]
            }]
           }
        
    @staticmethod
    def obtener_socio_id(id_socio):
        socios = Socio.objects(id=id_socio).get()
        dict_socio = dict()
        for socio in socios:
            dict_socio[socio] = socios[socio]
        return dict_socio

    @staticmethod
    def check_socio_dni(dni):
        socios = Socio(dni=dni)
        return socios

class Usuario(mongoengine.Document):
    usuario = mongoengine.StringField(required=True, max_length=50)
    passw = mongoengine.StringField(required=True, max_length=50)
    meta = {'collection':'usuarios'}

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
    def get_search_cobranzas(cls, data_cobranza: dict):
        cobranzas = []
        if data_cobranza["fecha_desde"] > data_cobranza["fecha_hasta"]:
            return []
        if len(data_cobranza["search_str"]):
            filters = (
                Q(nombre__icontains=data_cobranza["search_str"])
                | Q(apellido__icontains=data_cobranza["search_str"])
            ) & Q(activo__icontains=True)
            alumnos = Alumno.objects.filter(filters)

            if len(alumnos):
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
                        cobranzas.append(cobranza)
                return cobranzas
            else:
                return []
        else:
            filters = (
                Q(fechaCobranza__gte=data_cobranza["fecha_desde"])
                & Q(fechaCobranza__lte=data_cobranza["fecha_hasta"])
            ) & Q(isAnulada__icontains=data_cobranza["anulada"])
            return cls.objects.filter(filters)
DB().conectar()

#https://stackoverflow.com/questions/48621541/mongoengine-query-listfield-contains-string-matches

data_cobranza = dict()
data_cobranza['anulada'] = False
data_cobranza['search_str'] = "Acosta"
data_cobranza['fecha_desde'] = "2022-02-14"
data_cobranza['fecha_hasta'] = "2022-03-11"

for cobranza in Cobranza.get_search_cobranzas(data_cobranza):
    try:
        print(cobranza.alumno)
    except:
        for item in cobranza:
            print(item.alumno.apellido)
# str_search = "341"

# filters = Q(nombre__icontains=str_search) | Q(apellido__icontains=str_search)
# socios = Socio.objects.filter(filters)
# if(len(socios) == 0):
#     try:
#         str_search = int(str_search)
#         filters = Q(dni__icontains=str_search) | Q(telefono__icontains=str_search)
#         socios = Socio.objects.filter(filters)
#     except ValueError:
#         filters = Q(domicilio__icontains=str_search)
#         socios = Socio.objects.filter(filters)
# socios = Socio.objects.filter(__raw__={'$where': 'this.dni.toString().match({})'.format(str_search)})
# socios = Socio.objects.filter(__raw__={'$where': 'this.telefono.toString().match({})'.format(str_search)})
# socios = Socio.objects(Q(this.dni.toString()__icontains))
# for s in socios:
#     print(s.dni)

# except:
#     socio = "Sin resultados"

# if(isinstance(socio, str)):
#     print(socio)
# else:
# for s in socios:
    # print(s.dni)
#Eliminar socio y al mismo tiempo alumnos relacionados
# obj_socio = Socio.objects(dni=34836834).get()
# for list_alumnos in obj_socio.alumnos:
#     Alumno.objects(id=str(list_alumnos.id)).delete()
# obj_socio.delete()

#Eliminar Alumno y referencia en el array Socio
# obj_alumno = Alumno.objects(dni=48554887).get()
# obj_alumno.delete()

#Guardar socio y alumno
#list_alumno = Alumno(nombre = "Alvaro", apellido='Cortez',grado=3,dni=34765643,turno='Tarde',division='B',activo=1,ciclo=time.strftime("%Y"))
#list_alumno.save()
# socio = Socio(nombre="Ezequiel",apellido="Veamos",dni=738554389,domicilio='Alberdi 1022', telefono=3416887324)
# socio.alumnos.append(list_alumno.id)
# socio.save()

#Consulta completa
# obj_socio = Socio.objects(apellido='Acosta')
# for list_socio in obj_socio:
#     print(list_socio.dni)

# Actualizar socio
# obj_socio = Socio.objects(dni=29556349).get()
# obj_socio.update(nombre='Gabriel', apellido='Avila')

#Filtrar alumno
# obj_socio = Alumno.objects(apellido__iexact='Acosta').get()
# for list_alumno in obj_socio:
#     print(list_alumno)

# obj_socio = Socio.objects(apellido='Acosta')
# data_alumno = dict(apellido='Cortez',grado=3,dni=34765643,turno='Tarde',division='B',activo=1,ciclo=time.strftime("%Y"))
#
# obj_socio = Socio.objects(dni=34836834).get()
# list_alumno = Alumno(nombre='Daniel',apellido='Cortez',grado=3,dni=34765643,turno='Tarde',division='B',activo=1,ciclo=time.strftime("%Y"))
# list_alumno.save()
# obj_socio.alumnos.append(list_alumno.id)
# obj_socio.save()
# obj_socio.update(nombre="Ezequiel")
#
# id_alumno = Alumno.obtener_alumnos()[0].id
# print(Alumno.obtener_socio_alumno(id_alumno))

# print(Socio.obtener_socio_id("5dd2ce342cd7217db7436161"))

#Usuario(usuario='matias',passw='1234').save()
# list_alumno.save()
# if len(Socio.check_socio_dni(546789765)):
#     print('Es Objeto')
# else:
#     print('Es Array')

# print(Socio.check_socio_dni(45463235))