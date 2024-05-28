'''Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.'''
class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def dni(self):
        return self._dni
    
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("Nombre no tiene que estar vacio")
    
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("Edad no debe ser negativa")
    
    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str) and dni.isdigit():
            self._dni = dni
        else:
            raise ValueError("DNI No debe contener letras")
        
    def mostrar(self):
        print(f"Nombre: {self._nombre}"+f"Edad: {self._edad}"+f"DNI: {self._dni}")
    
    def es_mayor_de_edad(self):
        return self._edad >= 18

