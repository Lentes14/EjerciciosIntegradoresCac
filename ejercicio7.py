''' Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos. '''
from ejercicio6 import Persona
   
class Cuenta:

    def __init__(self, titular, cantidad=0):
        if not isinstance(titular, Persona):
            raise ValueError("Titular no es una instancia de Persona")
        self._titular = titular
        self._cantidad = float(cantidad)
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        print(f"Titular: {self._titular.nombre}")
        print(f"Cantidad: {self._cantidad:.2f}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        self._cantidad -= cantidad



