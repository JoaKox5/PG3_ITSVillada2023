def contar_vocales(frase):
    vocales = "a,e,i,o,u,A,E,I,O,U"
    cantidad = 0
    for letra in frase:
        if letra in vocales:
            cantidad += 1
    return cantidad

frase = "Hola mundo"
cantidad_vocales = contar_vocales(frase)
print(cantidad_vocales)