class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)

per1 = Persona('Juan')
per2 = Persona('Pedro')

per1.mostrar_nombre()
per2.mostrar_nombre()