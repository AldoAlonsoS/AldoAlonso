from mongoengine import *

connect('Padts')

class Estudiante(Document):
    nombre = StringField(required=True)
    correo = StringField(required=True)
    contraseña = StringField(required=True)


estudiante1 = Estudiante(
    nombre = 'Aldo', correo = 'aldoalonso@padts.com', contraseña = 'wwww'
)
estudiante2 = Estudiante(
    nombre = 'Juan', correo = 'Juan@padts.com', contraseña = 'xxxx'
)
estudiantes3 = Estudiante(
    nombre = 'Carlos', correo = 'Carlos@padts.com', contraseña = 'yyyy'
)
estudiantes4 = Estudiante(
    nombre = 'Martha', correo = 'Martha@padts.com', contraseña = 'zzzz'
)

def guardarestudiante():
    estudiante1.save()
    estudiante2.save()
    estudiantes3.save()
    estudiantes4.save()

def leerEstudiante():
    print(f'Nombre: {estudiante1.nombre} **Correo: {estudiante1.correo} **Contraseña: {estudiante1.contraseña}')
    print(f'Nombre: {estudiante2.nombre} **Correo: {estudiante2.correo} **Contraseña: {estudiante2.contraseña}')
    print(f'Nombre: {estudiantes3.nombre} **Correo: {estudiantes3.correo} **Contraseña: {estudiantes3.contraseña}')
    print(f'Nombre: {estudiantes4.nombre} **Correo: {estudiantes4.correo} **Contraseña: {estudiantes4.contraseña}')

def actualizaEstudiante():
    estudiante2.nombre = 'Bono'
    estudiante2.correo = 'Bono@padts.com'
    estudiante2.save()
    return print(f'===Actualizacion===\nNombre: {estudiante2.nombre} **Correo: {estudiante2.correo} **Contraseña: {estudiante2.contraseña}\n===Actualizacion correcta===')

def borrarEstudiante():
    estudiante2.delete()
    return Estudiante

guardarestudiante()
leerEstudiante()
actualizaEstudiante()
leerEstudiante()
borrarEstudiante()



#nombres = ['aldo', 'jesus', 'carlos', 'martha']
#correos = ['aldo@cinvestav.com', 'juan@cinvestav.com', 'carlos@cinvestav.com', 'martha@cinvestav.com']
#contraseñas = ['www','xxxx', 'yyyy', 'zzzz']

#for n,c,p in zip(nombres, correos, contraseñas):
#    registro = Estudiante(nombre=n ,correo=c, contraseña=p)
    #registro.save()

#estudiantes = Estudiante.objects

#for e in estudiantes:
#    print(f' Nombre: {e.nombre}\n Correo: {e.correo}\n Contraseña: {e.contraseña}' )


#estudiantes.save()
#print(estudiantes.correo)

