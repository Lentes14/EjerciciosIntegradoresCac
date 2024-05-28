''' Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia). '''
def contador_palabras(cadena):
    palabras = cadena.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    print (diccionario)

cadena=str(input("Ingresa cadena de caracteres:"))
contador_palabras(cadena)