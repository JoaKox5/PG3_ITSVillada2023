class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def imprimir_lado_mayor(self):
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado mayor es:", lado_mayor)
    
    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")

triangulo1 = Triangulo(5, 5, 5)
triangulo1.imprimir_lado_mayor()
triangulo1.es_equilatero()

triangulo2 = Triangulo(4, 6, 8)
triangulo2.imprimir_lado_mayor()
triangulo2.es_equilatero()