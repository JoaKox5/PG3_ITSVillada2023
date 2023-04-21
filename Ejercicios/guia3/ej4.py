try:
    numero1 = float(input("Ingresa un numero:  "))
    numero2 = float(input("Ingresa otro numero:  "))
        
    print(numero1 / numero2)
    
except ZeroDivisionError:
    print("No se puede dividir por cero")
    
except ValueError:
    print("Ingresa un numero")