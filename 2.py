# declaramos la clase persona
class Persona:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
#Declaramos la clase alumno
#Alumno hereda los atributos de la clase persona
class Alumno(Persona):
    def __init__(self):
        super().__init__()
        self.nota = int(input("Ingrese la nota del alumno"))

#Declaramos el metodo de mostrar
    
    def mostrar(self):
        super().mostrar()
        print("Nota: ")


#Declaramos el metodos de aprobacion de la nota
#Si el alumno tiene una nota mayor o igual a 3 aprueba
    def aprobacion(self):
        if self.nota >= 3:
            print("El alumno aprobo")
        else:
            print("El alumno no aprobo")

#Bloque principal
persona1 = Persona()
persona1.mostrar()
alumno1 = Alumno()
alumno1.mostrar()
alumno1.aprobacion()
