import mongoengine
from pymongo.errors import AutoReconnect, OperationFailure
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from mongoengine.queryset.visitor import Q

class Alumno(mongoengine.Document):
    nombre = mongoengine.StringField(required=True, max_length=50)
    apellido = mongoengine.StringField(required=True, max_length=50)
    grado = mongoengine.IntField(required=True, max_length=1)
    dni = mongoengine.IntField(required=True, max_length=8)
    turno = mongoengine.StringField(required=True, max_length=6)
    division = mongoengine.StringField(required=True, max_length=1)
    activo = mongoengine.BooleanField(required=True)
    ciclo = mongoengine.IntField(required=True, max_length=4)

    meta = {'collection':'alumnos',
            'indexes': [{
                'fields': ['$nombre', "$apellido", "$grado", "$turno", "$division"]
            }]
           }

    @classmethod
    def get_all_alumnos(cls):
        alumnos = cls.objects
        array_alumno = list()
        for alumno in alumnos:
            array_alumno.append(alumno)

        return array_alumno

    @classmethod
    def get_socio_by_alumno(cls, id_alumno):
        socio = Socio.objects(alumnos=id_alumno).get()
        return socio.apellido+', '+socio.nombre

    @classmethod
    def get_alumno_id(cls, id_alumno):
        return cls.objects(id=id_alumno).first()

    @classmethod
    def update_alumno_id(cls, data_alumno):
        try:
            obj_alumno = cls.objects(id=data_alumno['id']).get()
            obj_alumno.update(dni=data_alumno['dni'], apellido=data_alumno['apellido'],
                             nombre=data_alumno['nombre'], grado=data_alumno['grado'],
                             turno=data_alumno['turno'], division=data_alumno['division'])
            return "Alumno actualizado correctamente."
        except:
            return "Error al actualizar."

    @classmethod
    def delete_alumno(cls, id_alumno):
        obj_alumno = cls.objects(id=id_alumno).get()
        obj_alumno.delete()
        msj = "Datos del alumno eliminados correctamente."
        obj_socio = Socio.objects
        for socio in obj_socio:
            if len(socio.alumnos) == 0:
                Socio.objects(id=str(socio.id)).delete()
                msj = "Datos del alumno y el socio eliminados correctamente."

        return msj

    @classmethod
    def get_search_alumnos(cls, str_search):
        alumnos = []
        socios = []
        if(len(str_search) > 1):
            filters = (Q(nombre__icontains=str_search) | Q(apellido__icontains=str_search))
            alumnos = cls.objects.filter(filters)

        if(len(str_search) > 1 and len(alumnos) == 0):
            filters = Q(turno__icontains=str_search)
            alumnos = cls.objects.filter(filters)

        if(len(alumnos) == 0 and len(str_search) == 1):
            filters = Q(division__icontains=str_search)
            alumnos = cls.objects.filter(filters)

        if(len(alumnos) == 0):
            try:
                str_search = int(str_search)
                if(len(str(str_search)) == 1):
                    alumnos = cls.objects.filter(__raw__={'$where': 'this.grado.toString().match({})'.format(str_search)})
            except ValueError:
                alumnos = []

        if (len(str(str_search)) != 1):
            array_alumno = list()
            socios = Socio.get_search_socios(str_search)
            for socio in socios:
                for alumno_socio in socio.alumnos:
                    array_alumno.append(alumno_socio)

            if(array_alumno):
                return array_alumno

        if (len(alumnos) != 0):
            array_alumno = list()
            for alumno in alumnos:
                array_alumno.append(alumno)
            return array_alumno
        else:
            return cls.get_all_alumnos()


class Socio(mongoengine.Document):
    nombre = mongoengine.StringField(required=True, max_length=50)
    apellido = mongoengine.StringField(required=True, max_length=50)
    dni = mongoengine.IntField(required=True, max_length=8)
    domicilio = mongoengine.StringField(required=True, max_length=100)
    telefono = mongoengine.IntField(required=True, max_length=15)
    alumnos = mongoengine.ListField(mongoengine.ReferenceField('Alumno', reversedataSearchSocio_delete_rule=mongoengine.PULL))

    meta = {'collection':'socios',
            'indexes': [{
                'fields': ['$nombre', "$apellido", "$dni", "$domicilio", "$telefono"]
            }]
           }

    @classmethod
    def get_all_socios(cls):
        socios = cls.objects
        array_socio = list()
        for socio in socios:
            array_socio.append(socio)
        return array_socio

    @classmethod
    def get_socio_id(cls, id_socio):
        socios = cls.objects(id=id_socio).get()
        dict_socio = dict()
        for socio in socios:
            dict_socio[socio] = socios[socio]
        return dict_socio

    @classmethod
    def update_socio_id(cls, data_socio):
        try:
            obj_socio = cls.objects(id=data_socio['id']).get()
            obj_socio.update(dni=data_socio['dni'], apellido=data_socio['apellido'],
                             nombre=data_socio['nombre'], domicilio=data_socio['domicilio'],
                             telefono=data_socio['telefono'])
            return "Socio actualizado correctamente."
        except:
            return "Error al actualizar Socio."

    @classmethod
    def delete_socio(cls, id_socio):
        obj_socio = cls.objects(id=id_socio).get()
        for list_alumnos in obj_socio.alumnos:
            Alumno.objects(id=str(list_alumnos.id)).delete()
        obj_socio.delete()
        return "Datos del socio eliminados correctamente."

    @classmethod
    def get_search_socios(cls, str_search):
        filters = (Q(nombre__icontains=str_search) | Q(apellido__icontains=str_search))
        socios = cls.objects.filter(filters)

        if(len(socios) == 0):
            filters = Q(domicilio__icontains=str_search)
            socios = cls.objects.filter(filters)

        if(len(socios) == 0):
            try:
                str_search = int(str_search)
                socios = cls.objects.filter(__raw__={'$where': 'this.dni.toString().match({})'.format(str_search)})
            except ValueError:
                socios = []

        if (len(socios) == 0):
            try:
                str_search = int(str_search)
                socios = cls.objects.filter(__raw__={'$where': 'this.telefono.toString().match({})'.format(str_search)})
            except ValueError:
                socios = []

        if (len(socios) != 0):
            array_socio = list()
            for socio in socios:
                array_socio.append(socio)
            return array_socio
        else:
            return cls.get_all_socios()

class SocioThreadSave(QThread):
    statusSaveSocio = pyqtSignal((str,))
    def __init__(self):
        QThread.__init__(self)
        self.data_socio = None

    def check_socio_data(self, data_socio: dict):
        self.data_socio = data_socio

    def check_dict_socio(self, data_socio: dict):
        dict_check = True
        for value in data_socio.values():
            if value == '':
                dict_check = False
        return dict_check

    def run(self):
        #Guardamos socio y alumnos
        if self.check_dict_socio(self.data_socio):
            try:
                obj_socio = Socio.objects(dni=self.data_socio['dni_socio']).get()
                obj_alumno = Alumno(nombre=self.data_socio['nombre_alumno'],
                                    apellido=self.data_socio['apellido_alumno'],
                                    grado=self.data_socio['grado'], dni=self.data_socio['dni_alumno'],
                                    turno=self.data_socio['turno'],
                                    division=self.data_socio['division'], activo=True, ciclo=self.data_socio['ciclo'])
                obj_alumno.save()

                obj_socio.alumnos.append(obj_alumno.id)
                obj_socio.save()
                if self.data_socio['is_update']:
                    obj_socio.update(dni=self.data_socio['dni_socio'], apellido=self.data_socio['apellido_socio'],
                                  nombre=self.data_socio['nombre_socio'], domicilio=self.data_socio['domicilio_socio'],
                                  telefono=self.data_socio['telefono_socio'])
                self.statusSaveSocio.emit("")
            except mongoengine.DoesNotExist:
                obj_alumno = Alumno(nombre=self.data_socio['nombre_alumno'],
                                    apellido=self.data_socio['apellido_alumno'],
                                    grado=self.data_socio['grado'], dni=self.data_socio['dni_alumno'],
                                    turno=self.data_socio['turno'],
                                    division=self.data_socio['division'], activo=True, ciclo=self.data_socio['ciclo'])
                obj_alumno.save()

                obj_socio = Socio(dni=self.data_socio['dni_socio'], apellido=self.data_socio['apellido_socio'],
                                  nombre=self.data_socio['nombre_socio'], domicilio=self.data_socio['domicilio_socio'],
                                  telefono=self.data_socio['telefono_socio'])
                obj_socio.alumnos.append(obj_alumno.id)
                obj_socio.save()
                self.statusSaveSocio.emit("")
            except:
                self.statusSaveSocio.emit("Datos Incorrectos o incompletos.")
        elif self.data_socio['is_update']:
            try:
                obj_socio = Socio.objects(dni=self.data_socio['dni_socio']).get()
                obj_socio.update(dni=self.data_socio['dni_socio'], apellido=self.data_socio['apellido_socio'],
                                 nombre=self.data_socio['nombre_socio'], domicilio=self.data_socio['domicilio_socio'],
                                 telefono=self.data_socio['telefono_socio'])
                self.statusSaveSocio.emit("")
            except:
                self.statusSaveSocio.emit("Datos Incorrectos o incompletos.")
        else:
            self.statusSaveSocio.emit("Datos Incorrectos o incompletos.")


class SocioThreadUpdate(QThread):
    dataCheckSocio = pyqtSignal((dict,))
    statusCheckSocio = pyqtSignal((str,))
    def __init__(self):
        QThread.__init__(self)
        self.dni_socio = None

    def check_dni_socio(self, dni_socio: str):
        self.dni_socio = dni_socio

    def run(self):
        #Chequeamos si existe socio guardado con su dni.
        if self.dni_socio:
            try:
                socios = Socio.objects(dni=self.dni_socio).get()
                dict_socio = dict()
                for socio in socios:
                    dict_socio[socio] = socios[socio]
                self.dataCheckSocio.emit(dict_socio)
            except mongoengine.DoesNotExist:
                self.statusCheckSocio.emit("No existe socio.")
            except ValueError:
                self.statusCheckSocio.emit("Datos Incorrectos.")
        else:
            self.statusCheckSocio.emit("Campo vacio.")