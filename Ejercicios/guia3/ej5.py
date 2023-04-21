try:
        while True:
            with open("/home/thekvmaster/Programacion/Ejercicios/guia3/archivo.txt", "w") as archivo:
                dicc = {"Nombre": "Joaquin", "Apellido":"Parraga", "Edad": 17}
                numero = 17
                for c,v in dicc.items():
                    archivo.write(c + ":" + str(v) +"\n")
                archivo.write(numero)
except TypeError:
    print("No se puede ingresar un valor numerico, debes convertirlo a str")