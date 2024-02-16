# Clase que representa un nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


#Clase que representa un arbol binario ordenado
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # Método para insertar elementos
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_recursivo(valor, self.raiz)

    # Método auxiliar para insertar elementos
    def insertar_recursivo(self, valor, nodo_actual):
        if valor <= nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self.insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self.insertar_recursivo(valor, nodo_actual.derecha)

    # Método para buscar un elemento en el arbol
    def buscar(self, valor):
        return self.buscar_recursivo(valor, self.raiz)

    # Método auxiliar para buscar un elemento
    def buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self.buscar_recursivo(valor, nodo_actual.izquierda)
        else:
            return self.buscar_recursivo(valor, nodo_actual.derecha)

    # Método principal de pre-orden
    def preorden(self):
        resultado = []
        self.preorden_recursivo(self.raiz, resultado)
        return resultado

    # Método auxiliar de pre-orden
    def preorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            resultado.append(nodo_actual.valor)
            self.preorden_recursivo(nodo_actual.izquierda, resultado)
            self.preorden_recursivo(nodo_actual.derecha, resultado)

    # Método principal de in-orden
    def inorden(self):
        resultado = []
        self.inorden_recursivo(self.raiz, resultado)
        return resultado

    # Método auxiliar de in-orden
    def inorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            self.inorden_recursivo(nodo_actual.izquierda, resultado)
            resultado.append(nodo_actual.valor)
            self.inorden_recursivo(nodo_actual.derecha, resultado)

    # Método principal de pos-orden
    def postorden(self):
        resultado = []
        self.postorden_recursivo(self.raiz, resultado)
        return resultado

    # Método auxiliar de pos-orden
    def postorden_recursivo(self, nodo_actual, resultado):
        if nodo_actual:
            self.postorden_recursivo(nodo_actual.izquierda, resultado)
            self.postorden_recursivo(nodo_actual.derecha, resultado)
            resultado.append(nodo_actual.valor)

# ---------------------------------------------------------------------- #


# Variables globales que llevan la cuenta cuantos valles y montañas lleva.
valle = 0
montana = 0


# Método para resolver el problema de los valles y montañas
def problema_caminante(lista_recorrido):
    global valle
    global montana
    contador = 0

    for recorrido in lista_recorrido:
        if recorrido == "U":
            contador += 1
            if contador == 0:
                valle += 1
        if recorrido == "D":
            contador -= 1
            if contador == 0:
                montana += 1

    print("El número de montañas es "+str(montana)+" y el número de valles es "+str(valle))


if __name__ == "__main__":
    #arbol = ArbolBinario()
    #arbol.insertar(1)
    #arbol.insertar(10)
    #arbol.insertar(6)

    #for valor in arbol.inorden():
       #print(valor)

    lista = ["U", "U", "U", "D", "D", "D", "D", "U", "U", "U", "D", "D", "D", "D", "D", "U", "U", "U", "U", "U", "D"]
    problema_caminante(lista)
