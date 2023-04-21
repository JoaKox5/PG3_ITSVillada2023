meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

try:
    num_mes = int(input("Ingresa el número de mes (1-12): "))
    nombre_mes = meses[num_mes-1]
    
    print("El mes correspondiente es:", nombre_mes)
except IndexError:
    print("El numero debe estar entre 1 y 12")
except ValueError:
    print("El valor ingresado no es un numero")