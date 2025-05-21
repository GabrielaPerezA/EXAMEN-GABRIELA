from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.p = pasos  # pasos

    @abstractmethod
    def mostrar(self):
        pass


# Clase para recetas vegetarianas
class recetasVegetarianas(receta):
    def mostrar(self):
        print(f"Receta vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ingrediente in self.ingredientes: 
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas no vegetarianas
class recetasNoVegetarianas(receta):
    def mostrar(self):
        print(f"Receta NO vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase con utilidades del restaurante
class utilidades:
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for ingredientes_de_la_lista in lista:
            print(f"* {ingredientes_de_la_lista}")

# Función principal
def principal():
    receta1 = recetasVegetarianas("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta2 = recetasNoVegetarianas("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    elegir_receta = int(input("""que receta quieres elegir?:
                              1.receta vegetariana
                              2.receta no vegetariana"""))
    
    #hacemos un if, elif que pida al usuario la receta que quiera crear para eliminar las sentencias duplicadas.
    if elegir_receta == 1 :
        
        print("Ingredientes de Ensalada César:")
        for ingrediente in receta1.ingredientes:
            print(f"* {ingrediente}")
    elif elegir_receta == 2 : 
        print("Ingredientes de Pollo al horno:")
        for ingrediente in receta2.ingredientes:
            print(f"* {ingrediente}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
