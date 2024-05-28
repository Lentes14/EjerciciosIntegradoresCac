'''Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.'''
from ejercicio6 import Persona
from ejercicio7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        if isinstance(bonificacion, (int, float)) and 0 <= bonificacion <= 100:
            self._bonificacion = bonificacion
        else:
            raise ValueError("El numero no esta entre 0 y 100")
    
    def es_titular_valido(self):
        return self._titular.es_mayor_de_edad() and self._titular.edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Titular no valido para cuenta joven")
    
    def mostrar(self):
        super().mostrar()
        print(f"Cuenta Joven con una bonificación de {self._bonificacion}%")


