# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, nombre):
        self.vertices[nombre] = {}

    def agregar_arista(self, v1, v2, peso):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][v2] = peso
            self.vertices[v2][v1] = peso

    def obtener_arbol_expansion_minima(self):
        if not self.vertices:
            return []

        nodo_inicial = next(iter(self.vertices))
        visitados = set()
        arbol_expansion = []
        min_heap = [(0, nodo_inicial, None)] 
        total_peso = 0

        while min_heap:
            peso, nodo_actual, nodo_previo = heapq.heappop(min_heap)
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                total_peso += peso
                if nodo_previo is not None:
                    arbol_expansion.append((nodo_previo, nodo_actual, peso))

                for vecino, peso_arista in self.vertices[nodo_actual].items():
                    if vecino not in visitados:
                        heapq.heappush(min_heap, (peso_arista, vecino, nodo_actual))

        return arbol_expansion, total_peso

    def camino_mas_corto(self, inicio, fin):
        if inicio not in self.vertices or fin not in self.vertices:
            return None

        min_heap = [(0, inicio)]
        distancias = {nodo: float('inf') for nodo in self.vertices}
        distancias[inicio] = 0
        caminos = {nodo: None for nodo in self.vertices}

        while min_heap:
            peso_actual, nodo_actual = heapq.heappop(min_heap)

            if peso_actual > distancias[nodo_actual]:
                continue

            for vecino, peso_arista in self.vertices[nodo_actual].items():
                nueva_distancia = peso_actual + peso_arista
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    caminos[vecino] = nodo_actual
                    heapq.heappush(min_heap, (nueva_distancia, vecino))
        camino = []
        nodo = fin
        while nodo is not None:
            camino.append(nodo)
            nodo = caminos[nodo]
        camino.reverse()

        return camino, distancias[fin]

grafo = Grafo()

ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1",
    "baño 2", "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
]

for ambiente in ambientes:
    grafo.agregar_vertice(ambiente)

grafo.agregar_arista("cocina", "comedor", 5)
grafo.agregar_arista("cocina", "baño 1", 3)
grafo.agregar_arista("cocina", "cochera", 4)
grafo.agregar_arista("comedor", "quincho", 6)
grafo.agregar_arista("comedor", "sala de estar", 8)
grafo.agregar_arista("cochera", "habitación 1", 10)
grafo.agregar_arista("quincho", "terraza", 7)
grafo.agregar_arista("baño 1", "baño 2", 2)
grafo.agregar_arista("habitación 1", "habitación 2", 5)
grafo.agregar_arista("sala de estar", "patio", 9)

grafo.agregar_arista("habitación 1", "sala de estar", 12)
grafo.agregar_arista("habitación 2", "terraza", 15)
grafo.agregar_arista("baño 2", "patio", 4)

arbol_expansion, total_cable = grafo.obtener_arbol_expansion_minima()
# Imprimir el árbol de expansión mínima
print("Árbol de Expansión Mínima:")
for origen, destino, peso in arbol_expansion:
    print(f" - {origen} --({peso} metros)--> {destino}")
print(f"Total de metros de cable necesarios para conectar todos los ambientes: {total_cable} metros")

# Calcular y mostrar el camino más corto desde "habitación 1" hasta "sala de estar"
camino, distancia = grafo.camino_mas_corto("habitación 1", "sala de estar")
if camino:
    print("\nCamino más corto desde 'habitación 1' hasta 'sala de estar':")
    print(" -> ".join(camino))
    print(f"Distancia total: {distancia} metros")
else:
    print("No se encontró un camino desde 'habitación 1' hasta 'sala de estar'")

