# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.

def contar_palabras(cadena):
    palabras = cadena.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def palabra_mas_repetida(diccionario):
    max_palabra = max(diccionario, key=diccionario.get)
    frecuencia = diccionario[max_palabra]
    return (max_palabra, frecuencia)

cadena=str(input("Ingresa cadena de caracteres:"))
diccionario = contar_palabras(cadena)
print(diccionario)
palabra_repetida, frecuencia = palabra_mas_repetida(diccionario)
print("Palabra más repetida:", palabra_repetida, "Frecuencia:", frecuencia)