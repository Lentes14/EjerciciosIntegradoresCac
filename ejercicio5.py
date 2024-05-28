'''Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.'''

def get_int_ite():
    while True:
        try:
            a = int(input("Ingrese un valor entero: "))
            return a
        except ValueError:
            print("El valor ingresado no es un entero")

input = get_int_ite()
print("El valor entero ingresado es:", input)

def get_int_recur():
    try:
        a = int(input("Ingrese un valor entero: "))
        return a
    except ValueError:
        print("El valor ingresado no es un entero")
        return get_int_recur()

input = get_int_recur()
print("El valor entero ingresado es:", input)