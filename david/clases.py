#Creación de la clase Curso
class Curso:
    def __init__(self, c_code, c_name, c_duration):
        self.c_code=c_code
        self.c_name=c_name
        self.c_duration=c_duration
        self.clases = []

    def agregar_clase(self, clase):
        self.clases.append(clase)

#Creación de la clase Clase
class Clase:
    def __init__(self, num_class, type_class):
        self.num_class=num_class
        self.type_class=type_class

#Creación de la clase Online con herencia de Clase
class Online(Clase):
    def __init__(self, num_class, url):
        super().__init__(num_class, Online)
        self.url=url

#Creación de la clase Ftf con herencia de Clase
class Ftf(Clase):
    def __init__(self, num_class, total_std):
        super().__init__(num_class, Ftf)
        self.total_std=total_std

#Instanciando objetos
#Creación del curso
curso_python = Curso(21, "Python Basic", "40H")

#Creación de clases
clase_online = Online(11, "https://www.pruebaspython.net/clases")
clase_ftf = Ftf(12, 25)

#Agregar las clases al curso
curso_python.agregar_clase(clase_online)
curso_python.agregar_clase(clase_ftf)

print(curso_python)