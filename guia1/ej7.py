def es_numero_step(numero):
    cadena_numero = str(numero)
    for i in range(len(cadena_numero)-1):
        if abs(int(cadena_numero[i]) - int(cadena_numero[i+1])) != 1:
            return False
    return True

print(es_numero_step(9876787654))
