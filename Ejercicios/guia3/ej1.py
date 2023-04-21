try:
    while True:
        numero1 = int(input("Ingresa un numero:  "))
        numero2 = int(input("Ingresa otro numero:  "))

        print(numero1+numero2)

        pregunta = input("Deseas continuar sumando? Si/No")

        if(pregunta == "Si"):
            pass
        elif(pregunta == "No"):
            break
        else:
            print("No se ingreso lo solicitado")
            break
        
except ValueError:
    print("Ingresa un numero")
    