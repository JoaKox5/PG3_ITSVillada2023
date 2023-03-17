def pintar(ancho, alto, caracter):
    for i in range(alto): 
        for j in range(ancho):
            print(caracter, end="")
        print()

ancho = int(input("ingrese el ancho: "))
alto = int(input("ingrese el largo: "))
caracter = (input("ingrese el caracter: "))

print (pintar (ancho,alto,caracter))
