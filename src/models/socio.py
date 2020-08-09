import mongoengine
from PyQt5 import QtCore

class Alumno(mongoengine.Document):
    nombre = mongoengine.StringField(required=True, max_length=50)
    apellido = mongoengine.StringField(required=True, max_length=50)
    grado = mongoengine.IntField(required=True, max_length=1)
    dni = mongoengine.IntField(required=True, max_length=8)
    turno = mongoengine.StringField(required=True, max_length=6)
    division = mongoengine.StringField(required=True, max_length=1)
    activo = mongoengine.BooleanField(required=True)
    ciclo = mongoengine.IntField(required=True, max_length=4)
    meta = {'collection':'alumnos'}

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

    @staticmethod
    def obtener_alumno_id(id_alumno):
        alumnos = Alumno.objects(id=id_alumno).get()
        dict_alumno = dict()
        for alumno in alumnos:
            dict_alumno[alumno] = alumnos[alumno]
        return dict_alumno

    @staticmethod
    def update_alumno_id(data_alumno):
        try:
            obj_alumno = Alumno.objects(id=data_alumno['id']).get()
            obj_alumno.update(dni=data_alumno['dni'], apellido=data_alumno['apellido'],
                             nombre=data_alumno['nombre'], grado=data_alumno['grado'],
                             turno=data_alumno['turno'], division=data_alumno['division'])
            return "Alumno actualizado correctamente."
        except:
            return "Error al actualizar."

    @staticmethod
    def delete_alumno(id_alumno):
        obj_alumno = Alumno.objects(id=id_alumno).get()
        obj_alumno.delete()
        msj = "Datos del alumno eliminados correctamente."
        obj_socio = Socio.objects
        for socio in obj_socio:
            if len(socio.alumnos) == 0:
                Socio.objects(id=str(socio.id)).delete()
                msj = "Datos del alumno y el socio eliminados correctamente."

        return msj


class Socio(mongoengine.Document):
    nombre = mongoengine.StringField(required=True, max_length=50)
    apellido = mongoengine.StringField(required=True, max_length=50)
    dni = mongoengine.IntField(required=True, max_length=8)
    domicilio = mongoengine.StringField(required=True, max_length=100)
    telefono = mongoengine.IntField(required=True, max_length=15)
    alumnos = mongoengine.ListField(mongoengine.ReferenceField('Alumno', reverse_delete_rule=mongoengine.PULL))
    meta = {'collection':'socios'}

    @staticmethod
    def obtener_socios():
        socios = Socio.objects
        array_socio = list()
        for socio in socios:
            array_socio.append(socio)
        return array_socio

    @staticmethod
    def obtener_socio_id(id_socio):
        socios = Socio.objects(id=id_socio).get()
        dict_socio = dict()
        for socio in socios:
            dict_socio[socio] = socios[socio]
        return dict_socio

    @staticmethod
    def update_socio_id(data_socio):
        try:
            obj_socio = Socio.objects(id=data_socio['id']).get()
            obj_socio.update(dni=data_socio['dni'], apellido=data_socio['apellido'],
                             nombre=data_socio['nombre'], domicilio=data_socio['domicilio'],
                             telefono=data_socio['telefono'])
            return "Socio actualizado correctamente."
        except:
            return "Error al actualizar."

    @staticmethod
    def delete_socio(id_socio):
        obj_socio = Socio.objects(id=id_socio).get()
        for list_alumnos in obj_socio.alumnos:
            Alumno.objects(id=str(list_alumnos.id)).delete()
        obj_socio.delete()
        return "Datos del socio eliminados correctamente."


class SocioThreadSave(QtCore.QThread):
    statusSaveSocio = QtCore.pyqtSignal((str,))
    def __init__(self):
        QtCore.QThread.__init__(self)
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


class SocioThreadUpdate(QtCore.QThread):
    dataCheckSocio = QtCore.pyqtSignal((dict,))
    statusCheckSocio = QtCore.pyqtSignal((str,))
    def __init__(self):
        QtCore.QThread.__init__(self)
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