# 15. Se requ expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país iere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol detiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_maravilla(self, nombre, tipo, paises):
        self.vertices[nombre] = {
            'tipo': tipo,
            'paises': set(paises),
            'adyacentes': {}
        }

    def agregar_conexion(self, nombre1, nombre2, distancia):
        if nombre1 in self.vertices and nombre2 in self.vertices:
            tipo1 = self.vertices[nombre1]['tipo']
            tipo2 = self.vertices[nombre2]['tipo']
            if tipo1 == tipo2:  # Solo conectar si son del mismo tipo
                self.vertices[nombre1]['adyacentes'][nombre2] = distancia
                self.vertices[nombre2]['adyacentes'][nombre1] = distancia

    def obtener_arbol_expansion_minimo(self, tipo):
        import heapq
        
        vertices_tipo = {k: v for k, v in self.vertices.items() if v['tipo'] == tipo}
        if not vertices_tipo:
            return None
        
        nodo_inicial = next(iter(vertices_tipo))
        visitados = set()
        arbol_expansion = []
        min_heap = [(0, nodo_inicial, None)]

        while min_heap and len(visitados) < len(vertices_tipo):
            distancia, nodo_actual, nodo_previo = heapq.heappop(min_heap)
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                if nodo_previo:
                    arbol_expansion.append((nodo_previo, nodo_actual, distancia))

                for vecino, peso in self.vertices[nodo_actual]['adyacentes'].items():
                    if vecino not in visitados:
                        heapq.heappush(min_heap, (peso, vecino, nodo_actual))

        return arbol_expansion

    def paises_con_maravillas_ambos_tipos(self):
        paises_arquitectonicas = set()
        paises_naturales = set()

        for datos in self.vertices.values():
            if datos['tipo'] == 'arquitectónica':
                paises_arquitectonicas.update(datos['paises'])
            elif datos['tipo'] == 'natural':
                paises_naturales.update(datos['paises'])

        return paises_arquitectonicas & paises_naturales  # Intersección

    def paises_con_multiples_maravillas_mismo_tipo(self):
        maravillas_por_pais = {}

        for nombre, datos in self.vertices.items():
            for pais in datos['paises']:
                if pais not in maravillas_por_pais:
                    maravillas_por_pais[pais] = {'arquitectónica': 0, 'natural': 0}
                maravillas_por_pais[pais][datos['tipo']] += 1

        paises_multiples = {
            pais for pais, conteo in maravillas_por_pais.items() 
            if conteo['arquitectónica'] > 1 or conteo['natural'] > 1
        }

        return paises_multiples

# Ejemplo de uso
grafo = Grafo()

# Agregamos las maravillas arquitectónicas
grafo.agregar_maravilla("Gran Muralla China", "arquitectónica", ["China"])
grafo.agregar_maravilla("Cristo Redentor", "arquitectónica", ["Brasil"])
grafo.agregar_maravilla("Machu Picchu", "arquitectónica", ["Perú"])
grafo.agregar_maravilla("Chichen Itza", "arquitectónica", ["México"])
grafo.agregar_maravilla("Coliseo", "arquitectónica", ["Italia"])
grafo.agregar_maravilla("Taj Mahal", "arquitectónica", ["India"])
grafo.agregar_maravilla("Petra", "arquitectónica", ["Jordania"])

# Agregamos las maravillas naturales
grafo.agregar_maravilla("Amazonas", "natural", ["Brasil", "Perú", "Colombia"])
grafo.agregar_maravilla("Bahía de Ha Long", "natural", ["Vietnam"])
grafo.agregar_maravilla("Cataratas del Iguazú", "natural", ["Argentina", "Brasil"])
grafo.agregar_maravilla("Isla Jeju", "natural", ["Corea del Sur"])
grafo.agregar_maravilla("Parque Nacional de Komodo", "natural", ["Indonesia"])
grafo.agregar_maravilla("Montaña de la Mesa", "natural", ["Sudáfrica"])
grafo.agregar_maravilla("Río subterráneo de Puerto Princesa", "natural", ["Filipinas"])

# Agregamos conexiones con distancias de ejemplo entre maravillas del mismo tipo
grafo.agregar_conexion("Gran Muralla China", "Cristo Redentor", 17500)
grafo.agregar_conexion("Cristo Redentor", "Machu Picchu", 3310)

print("Árbol de expansión mínimo - Arquitectónicas:", grafo.obtener_arbol_expansion_minimo("arquitectónica"))
print("Árbol de expansión mínimo - Naturales:", grafo.obtener_arbol_expansion_minimo("natural"))

# b. Países con maravillas de ambos tipos
print("Países con maravillas arquitectónicas y naturales:", grafo.paises_con_maravillas_ambos_tipos())

# c. Países con más de una maravilla del mismo tipo
print("Países con múltiples maravillas del mismo tipo:", grafo.paises_con_multiples_maravillas_mismo_tipo())