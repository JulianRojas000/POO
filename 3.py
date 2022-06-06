#Definimos la clase de calculadora
class calculadora:
    def __init__(self):
        self.num_1 = int(input("Ingrese un numero"))
        self.num_2 = int(input("Ingrese otro numero"))
    #Definimos las operaciones como metodos
    def suma(self):
        suma = self.num_1 + self.num_2
        print("la suma de los numeros es: ", suma)

    def resta(self):
        resta = self.num_1 - self.num_2
        print("la resta de los numeros es: ", resta)

    def multi(self):
        multi = self.num_1 * self.num_2
        print("la multiplicacion de los numeros es: ", multi)

    def divi(self):
        divi = self.num_1 / self.num_2
        print("la division de los numeros es: ", divi)
#Bloque principal
operaciones = calculadora()
operaciones.suma()
operaciones.resta()
operaciones.multi()
operaciones.divi()
