class Familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
        
    def __str__(self):
        return "Padre:",self.padre,"Madre:",self.madre,"Hijos:",self.hijos
    

hijos = ['Pedro', 'Juancito', 'Pedrito', 'Juan']

familia1 = Familia('Jose', 'Sofia', hijos)
print(familia1.__str__())
