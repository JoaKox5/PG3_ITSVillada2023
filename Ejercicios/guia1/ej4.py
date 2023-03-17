def ordenar_lista(lista):
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada


lista = [3,8,9,12,5,7]
lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)