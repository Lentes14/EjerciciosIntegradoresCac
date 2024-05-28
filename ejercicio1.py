# Escribir una función que calcule el máximo común divisor entre dos números.

import math

def maximoComunDivisor(a, b):
    print(f"El maximo comun divisor de {a} y {b} es:", math.gcd(a,b))
    

print("Calcular maximo comun divisor")
a=int(input("Ingresa el primer numero:"))
b=int(input("Ingreso el segundo numero:"))
maximoComunDivisor(a, b)