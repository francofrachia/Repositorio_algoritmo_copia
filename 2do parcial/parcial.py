from collections import defaultdict
#RESOLUCIÓN PUNTO 1

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_rec(self.root, data)

    def _insert_rec(self, node, data):
        if data["numero"] < node.data["numero"]:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_rec(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_rec(node.right, data)

    def inorder(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        if node is None:
            return []
        return self._inorder_rec(node.left) + [node.data] + self._inorder_rec(node.right)

pokemons = [
    {"numero": 1, "nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
    {"numero": 2, "nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"},
    {"numero": 3, "nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
    {"numero": 4, "nombre": "Starmie", "nivel": 30, "tipo": "Agua", "subtipo": "Psíquico"},
    {"numero": 5, "nombre": "Psyduck", "nivel": 25, "tipo": "Agua", "subtipo": None},
    {"numero": 6, "nombre": "Gyarados", "nivel": 35, "tipo": "Agua", "subtipo": "Volador"},
    {"numero": 7, "nombre": "Onix", "nivel": 38, "tipo": "Roca", "subtipo": "Tierra"},
    {"numero": 8, "nombre": "Geodude", "nivel": 28, "tipo": "Roca", "subtipo": "Tierra"},
    {"numero": 9, "nombre": "Vulpix", "nivel": 20, "tipo": "Fuego", "subtipo": None},
    {"numero": 10, "nombre": "Blastoise", "nivel": 50, "tipo": "Agua", "subtipo": None},
    {"numero": 11, "nombre": "Umbreon", "nivel": 45, "tipo": "Siniestro", "subtipo": None},
    {"numero": 12, "nombre": "Nidoking", "nivel": 40, "tipo": "Veneno", "subtipo": "Tierra"},
    {"numero": 13, "nombre": "Jolteon", "nivel": 50, "tipo": "Eléctrico", "subtipo": None},
    {"numero": 14, "nombre": "Lycanroc", "nivel": 45, "tipo": "Roca", "subtipo": None},
    {"numero": 15, "nombre": "Tyrantrum", "nivel": 55, "tipo": "Roca", "subtipo": "Dragón"},
    {"numero": 16, "nombre": "Gardevoir", "nivel": 48, "tipo": "Psíquico", "subtipo": "Hada"},
    {"numero": 17, "nombre": "Raichu", "nivel": 60, "tipo": "Eléctrico", "subtipo": None},
]

tree_by_name = BinaryTree()
tree_by_number = BinaryTree()
tree_by_type = defaultdict(BinaryTree)

for pokemon in pokemons:
    tree_by_name.insert(pokemon)
    tree_by_number.insert(pokemon)
    tree_by_type[pokemon["tipo"]].insert(pokemon)

def search_by_proximity(tree, name_part):
    results = []
    
    def _search(node):
        if node:
            if name_part in node.data["nombre"].lower(): 
                results.append(node.data)
            _search(node.left)
            _search(node.right)
    
    _search(tree.root)
    return results

def get_pokemons_by_type(tree, tipo):
    results = []
    
    def _search(node):
        if node:
            if node.data["tipo"] == tipo:
                results.append(node.data["nombre"])
            _search(node.left)
            _search(node.right)
    
    _search(tree.root)
    return results

def count_pokemons_by_type(pokemons, tipo):
    return sum(1 for pokemon in pokemons if pokemon["tipo"] == tipo)

def main():
    # b) Búsqueda por proximidad
    print("\nRESOLUCIÓN PUNTO B")
    print("Buscar Pokémon por proximidad (\"bul\"):")
    matching_pokemon = search_by_proximity(tree_by_name, "bul")
    for pokemon in matching_pokemon:
        print(pokemon)

    # c) Mostrar Pokémon de tipo específico
    print("\nRESOLUCIÓN PUNTO C")
    tipos = ["Agua", "Fuego", "Planta", "Eléctrico"]
    for tipo in tipos:
        print(f"Pokémon de tipo {tipo}:")
        type_pokemons = get_pokemons_by_type(tree_by_type[tipo], tipo)
        for nombre in type_pokemons:
            print(nombre)

    # d) Listados en orden ascendente
    print("\nRESOLUCIÓN PUNTO D")
    print("Listado en orden ascendente por número:")
    for pokemon in tree_by_number.inorder():
        print(f"{pokemon['numero']}: {pokemon['nombre']}")

    print("\nListado por nivel:")
    sorted_by_level = sorted(pokemons, key=lambda x: (x['nivel'], x['nombre']))
    for pokemon in sorted_by_level:
        print(f"{pokemon['nivel']}: {pokemon['nombre']}")

    # e) Mostrar datos de Pokémon específicos
    print("\nRESOLUCIÓN PUNTO E")
    specific_pokemons = ["Jolteon", "Lycanroc", "Tyrantrum"]
    print("Datos de Pokémon específicos:")
    for name in specific_pokemons:
        for pokemon in pokemons:
            if pokemon['nombre'] == name:
                print(pokemon)

    # f) Contar Pokémon de tipo eléctrico y acero
    print("\nRESOLUCIÓN PUNTO F")
    electric_count = count_pokemons_by_type(pokemons, "Eléctrico")
    steel_count = count_pokemons_by_type(pokemons, "Acero") 

    print(f"Cantidad de Pokémon de tipo Eléctrico: {electric_count}")
    print(f"Cantidad de Pokémon de tipo Acero: {steel_count}")


if __name__ == "__main__":
    main()


#RESOLUCIÓN PUNTO 2:

import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        self.adjacency_list[from_vertex].append((to_vertex, weight))
        self.adjacency_list[to_vertex].append((from_vertex, weight))

    def minimum_spanning_tree(self):
        mst = []  
        visited = set()
        min_heap = [(0, next(iter(self.adjacency_list)))]  
        prev_vertex = None

        while min_heap:
            weight, current_vertex = heapq.heappop(min_heap)
            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            if prev_vertex is not None:
                mst.append((prev_vertex, current_vertex, weight))  

            for neighbor, edge_weight in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
                    
            prev_vertex = current_vertex  

        return mst, 'Yoda' in visited  

    def max_shared_episodes(self):
        max_weight = 0
        characters_pair = ("", "")
        for vertex in self.adjacency_list:
            for neighbor, weight in self.adjacency_list[vertex]:
                if weight > max_weight:
                    max_weight = weight
                    characters_pair = (vertex, neighbor)
        
        return max_weight, characters_pair



graph = Graph()


characters = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett",
    "C-3PO", "Leia", "Kylo Ren", "Chewbacca",
    "Han Solo", "R2-D2", "BB-8", "Rey" 
]

for character in characters:
    graph.add_vertex(character)


edges = [
    ("Luke Skywalker", "Yoda", 4),
    ("Luke Skywalker", "Leia", 3),
    ("Leia", "Han Solo", 4),
    ("Han Solo", "Chewbacca", 5),
    ("Yoda", "Darth Vader", 3),
    ("Darth Vader", "Boba Fett", 2),
    ("C-3PO", "R2-D2", 2),
    ("Rey", "Kylo Ren", 2),
    ("BB-8", "C-3PO", 1)
]

for from_vertex, to_vertex, weight in edges:
    graph.add_edge(from_vertex, to_vertex, weight)

# PUNTO B
mst, contains_yoda = graph.minimum_spanning_tree()
print("\nPUNTO 2")
print("\nRESOLUCIÓN PUNTO B")
print("Árbol de expansión mínimo (MST):")
for from_vertex, to_vertex, weight in mst:
    print(f"{from_vertex} -- {to_vertex} (Peso: {weight})")


if contains_yoda:
    print("\nYoda está incluido en el árbol de expansión mínimo.")
else:
    print("\nYoda NO está incluido en el árbol de expansión mínimo.")

# PUNTO C
max_episodes, characters_pair = graph.max_shared_episodes()

print("\nRESOLUCIÓN PUNTO C")
print(f"Máximo número de episodios compartidos: {max_episodes}")
print(f"Personajes que comparten este número de episodios: {characters_pair[0]} y {characters_pair[1]}")
