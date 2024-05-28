# Escribir una función que calcule el mínimo común múltiplo entre dos números

import math

def minimoComunMultiplo(a, b):
    print(f"El mínimo común múltiplo de {a} y {b} es:", math.lcm(a,b))


print("Calcular mínimo común múltiplo")
a=int(input("Ingresa el primer numero:"))
b=int(input("Ingreso el segundo numero:"))   
minimoComunMultiplo(a, b)
