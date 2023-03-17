def buscar_valor(lista, valor):

    indice = lista.index(valor)
    return indice

lista = [8, 4, 9, 122,5,12,0]
valor = 12
indice = buscar_valor(lista, valor)

if indice == -1:
    print("El valor no se encuentra en la lista.")
else:
    print(f"El valor se encuentra en la posición {indice}.")