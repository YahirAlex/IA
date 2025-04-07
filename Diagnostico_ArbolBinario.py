class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def vacio(self):
        return self.raiz is None

    def insertar(self, nombre):
        if self.vacio():
            self.raiz = Nodo(nombre)
        else:
            self._insertarRec(self.raiz, nombre)

    def _insertarRec(self, nodo, nombre):
        if nombre < nodo.nombre:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nombre)
            else:
                self._insertarRec(nodo.izquierda, nombre)
        elif nombre > nodo.nombre:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nombre)
            else:
                self._insertarRec(nodo.derecha, nombre)

    def buscarNodo(self, nombre):
        return self._buscarPorInorden(self.raiz, nombre)

    def _buscarPorInorden(self, nodo, nombre):
        if nodo is not None:
            resultado = self._buscarPorInorden(nodo.izquierda, nombre)
            if resultado:
                return resultado
            if nodo.nombre == nombre:
                return nodo
            return self._buscarPorInorden(nodo.derecha, nombre)
        return None

# ⚙️ Uso del árbol con 10 nombres distintos
arbol = Arbol()
nombres = ["Leonardo", "Valeria", "Hugo", "Camila", "Santiago",
           "Diana", "Gabriel", "Ximena", "Isabela", "Bruno"]

for nombre in nombres:
    arbol.insertar(nombre)

# Buscar uno de ellos
nodo = arbol.buscarNodo("Gabriel")
if nodo:
    print(f"Nodo se ha encontrado: {nodo.nombre}")
else:
    print("Nodo no hacido encontrado")
print(f"¿El árbol se encuentra vacio? {arbol.vacio()}")
