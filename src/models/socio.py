from datetime import date

import mongoengine
from PyQt5.QtCore import pyqtSignal, QThread
from mongoengine.queryset.visitor import Q

class Socio(mongoengine.Document):
    nombre = mongoengine.StringField(required=True, max_length=50)
    apellido = mongoengine.StringField(required=True, max_length=50)
    dni = mongoengine.IntField(required=True, max_length=8)
    domicilio = mongoengine.StringField(required=True, max_length=100)
    telefono = mongoengine.IntField(required=True, max_length=15)
    activo = mongoengine.BooleanField(required=True)
    alumnos = mongoengine.ListField(mongoengine.ReferenceField('Alumno', reversedataSearchSocio_delete_rule=mongoengine.PULL))

    meta = {'collection':'socios',
            'indexes': [{
                'fields': ['$nombre', "$apellido", "$dni", "$domicilio", "$telefono"]
            }]
           }

    @classmethod
    def get_all_socios(cls):
        socios = cls.objects(activo=True)
        array_socio = list()
        for socio in socios:
            array_socio.append(socio)
        return array_socio

    @classmethod
    def get_all_socios_name(cls):
        socios = cls.objects(activo=True)
        array_socio = list()
        for socio in socios:
            dict_socio = dict()
            dict_socio['id'] = socio.id
            dict_socio['socio'] = socio.apellido+', '+socio.nombre
            array_socio.append(dict_socio)
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
            obj_alumno = Alumno.objects(id=str(list_alumnos.id)).get()
            obj_alumno.activo = not obj_alumno.activo
            obj_alumno.update(activo=obj_alumno.activo)
        if obj_socio.activo:
            msj = "Datos del socio inactivados correctamente."
        else:
            msj = "Datos del socio activados correctamente."
        obj_socio.activo = not obj_socio.activo
        obj_socio.update(activo=obj_socio.activo)
        return msj

    @classmethod
    def get_search_socios(cls, str_search, check_socio):
        filters = ((Q(nombre__icontains=str_search) | Q(apellido__icontains=str_search)) & Q(activo__icontains=check_socio))
        socios = cls.objects.filter(filters)

        if(len(socios) == 0):
            filters = Q(domicilio__icontains=str_search) & Q(activo__icontains=check_socio)
            socios = cls.objects.filter(filters)

        if(len(socios) == 0):
            try:
                str_search = int(str_search)
                socios = cls.objects.filter(Q(__raw__={'$where': 'this.dni.toString().match({})'.format(str_search)}) & Q(activo__icontains=check_socio))
            except ValueError:
                socios = []

        if (len(socios) == 0):
            try:
                str_search = int(str_search)
                socios = cls.objects.filter(Q(__raw__={'$where': 'this.telefono.toString().match({})'.format(str_search)}) & Q(activo__icontains=check_socio))
            except ValueError:
                socios = []

        if (len(socios) != 0):
            array_socio = list()
            for socio in socios:
                array_socio.append(socio)
            return array_socio
        elif len(str_search) == 0:
            array_socio = list()
            socios = cls.objects.filter(activo__icontains=check_socio)
            for socio in socios:
                array_socio.append(socio)
            return array_socio
        else:
            return []

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
        #Guardamos socio
        if self.check_dict_socio(self.data_socio):

            try:
                if(len(Socio.objects(dni=self.data_socio['dni_socio']))):
                    self.statusSaveSocio.emit("DNI Existente.")
                else:
                    obj_socio = Socio(dni=self.data_socio['dni_socio'], apellido=self.data_socio['apellido_socio'],
                                      nombre=self.data_socio['nombre_socio'], domicilio=self.data_socio['domicilio_socio'],
                                      telefono=self.data_socio['telefono_socio'], activo=True)
                    obj_socio.save()
                    self.statusSaveSocio.emit("")
            except:
                self.statusSaveSocio.emit("Datos Incorrectos o incompletos.")
        else:
            self.statusSaveSocio.emit("Datos Incorrectos o incompletos.")


# Model Alumno
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
        alumnos = cls.objects(activo=True)
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
        alumno_data = cls.objects(id=id_alumno).get()
        socio = Socio.objects(alumnos=id_alumno).get()

        dict_alumno = dict()
        dict_alumno['socio'] =  socio.apellido+', '+socio.nombre

        for alumno in alumno_data:
            dict_alumno[alumno] = alumno_data[alumno]

        return dict_alumno


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
        if obj_alumno.activo:
            msj = "Datos del alumno inactivados correctamente."
        else:
            msj = "Datos del alumno activados correctamente."
        obj_alumno.activo = not obj_alumno.activo
        obj_alumno.update(activo=obj_alumno.activo)
        obj_socio = Socio.objects.get(alumnos__contains=obj_alumno.id)

        check_inactive_alumnos = True
        for list_alumnos in obj_socio.alumnos:
            obj_alumno_check = cls.objects(id=list_alumnos.id).get()
            if obj_alumno_check.activo:
                check_inactive_alumnos = False

        if check_inactive_alumnos:
            if obj_alumno.activo:
                msj = "Datos del alumno y el socio activados correctamente."
            else:
                msj = "Datos del alumno y el socio inactivados correctamente."
            obj_socio.activo = not obj_socio.activo
            obj_socio.update(activo=obj_socio.activo)

        if not obj_socio.activo and obj_alumno.activo:
            obj_socio.activo = not obj_socio.activo
            obj_socio.update(activo=obj_socio.activo)
        return msj

    @classmethod
    def get_search_alumnos(cls, str_search, check_alumno):
        alumnos = []
        socios = []
        if(len(str_search) > 1):
            filters = ((Q(nombre__icontains=str_search) | Q(apellido__icontains=str_search)) & Q(activo__icontains=check_alumno))
            alumnos = cls.objects.filter(filters)

        if(len(str_search) > 1 and len(alumnos) == 0):
            filters = (Q(turno__icontains=str_search) & Q(activo__icontains=check_alumno))
            alumnos = cls.objects.filter(filters)

        if(len(alumnos) == 0 and len(str_search) == 1):
            filters = (Q(division__icontains=str_search) & Q(activo__icontains=check_alumno))
            alumnos = cls.objects.filter(filters)

        if(len(alumnos) == 0):
            try:
                str_search = int(str_search)
                if(len(str(str_search)) == 1):
                    alumnos = cls.objects.filter(Q(__raw__={'$where': 'this.grado.toString().match({})'.format(str_search)}) & Q(activo__icontains=check_alumno))
            except ValueError:
                alumnos = []

        if (len(str(str_search)) != 1):
            array_alumno = list()
            print(str_search, check_alumno)
            socios = Socio.get_search_socios(str_search, check_alumno)
            for socio in socios:
                for alumno_socio in socio.alumnos:
                    if alumno_socio.activo:
                        array_alumno.append(alumno_socio)

            if(array_alumno):
                return array_alumno

        if len(alumnos) != 0:
            array_alumno = list()
            for alumno in alumnos:
                array_alumno.append(alumno)
            return array_alumno
        elif len(str_search) == 0:
            array_alumno = list()
            alumnos = cls.objects.filter(activo__icontains=check_alumno)
            for alumno in alumnos:
                array_alumno.append(alumno)
            return array_alumno
        else:
            return []


class AlumnoThreadSave(QThread):
    statusSaveAlumno = pyqtSignal((str,))
    def __init__(self):
        QThread.__init__(self)
        self.data_alumno = None

    def check_alumno_data(self, data_alumno: dict):
        self.data_alumno = data_alumno

    def check_dict_alumno(self, data_alumno: dict):
        dict_check = True
        for value in data_alumno.values():
            if value == '':
                dict_check = False
        return dict_check

    def run(self):
        #Guardamos socio
        if self.check_dict_alumno(self.data_alumno):
            self.today = date.today()
            try:
                if(len(Alumno.objects(dni=self.data_alumno['dni']))):
                    self.statusSaveAlumno.emit("DNI Existente.")
                else:
                    obj_alumno = Alumno(dni=self.data_alumno['dni'], apellido=self.data_alumno['apellido'],
                                      nombre=self.data_alumno['nombre'], grado=self.data_alumno['grado'],
                                      turno=self.data_alumno['turno'], division=self.data_alumno['division'],
                                      ciclo=self.today.year, activo=True)
                    obj_alumno.save()
                    obj_socio = Socio.objects(id=self.data_alumno['socio']).get()
                    obj_socio.alumnos.append(obj_alumno.id)
                    obj_socio.save()

                    self.statusSaveAlumno.emit("")
            except:
                self.statusSaveAlumno.emit("Datos Incorrectos o incompletos.")
        else:
            self.statusSaveAlumno.emit("Datos Incorrectos o incompletos.")