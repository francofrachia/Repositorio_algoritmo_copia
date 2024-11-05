from tp2.pila import Stack

def encontrar_posicion(pila, nombre):
    temp_pila = Stack()
    posicion = 1
    encontrado = False

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['nombre'] == nombre:
            encontrado = True
            break
        posicion += 1

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return posicion if encontrado else None

def personajes_mas_de_5_peliculas(pila):
    temp_pila = Stack()
    personajes = []

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['peliculas'] > 5:
            personajes.append(personaje)

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return personajes

def peliculas_black_widow(pila):
    temp_pila = Stack()
    peliculas = 0

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['nombre'] == 'Black Widow':
            peliculas = personaje['peliculas']
            break

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return peliculas

def personajes_nombres_CDG(pila):
    temp_pila = Stack()
    personajes = []

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['nombre'][0] in ['C', 'D', 'G']:
            personajes.append(personaje)

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return personajes

pila_personajes = Stack()

personajes_mcu = [
    {'nombre': 'Iron Man', 'peliculas': 10},
    {'nombre': 'Captain America', 'peliculas': 9},
    {'nombre': 'Black Widow', 'peliculas': 8},
    {'nombre': 'Thor', 'peliculas': 7},
    {'nombre': 'Hulk', 'peliculas': 6},
    {'nombre': 'Hawkeye', 'peliculas': 5},
    {'nombre': 'Rocket Raccoon', 'peliculas': 4},
    {'nombre': 'Groot', 'peliculas': 4},
    {'nombre': 'Doctor Strange', 'peliculas': 3},
    {'nombre': 'Spider-Man', 'peliculas': 5},
]

for personaje in personajes_mcu:
    pila_personajes.push(personaje)

# a.
pos_rocket = encontrar_posicion(pila_personajes, 'Rocket Raccoon')
pos_groot = encontrar_posicion(pila_personajes, 'Groot')

print(f"Posición de Rocket Raccoon: {pos_rocket}")
print(f"Posición de Groot: {pos_groot}")

# b.
mas_de_5_peliculas = personajes_mas_de_5_peliculas(pila_personajes)
print("Personajes que participaron en más de 5 películas:")
for personaje in mas_de_5_peliculas:
    print(f"{personaje['nombre']} participó en {personaje['peliculas']} películas")

# c.
peliculas_bw = peliculas_black_widow(pila_personajes)
print(f"Black Widow participó en {peliculas_bw} películas")

# d.
personajes_cdg = personajes_nombres_CDG(pila_personajes)
print("Personajes cuyos nombres empiezan con C, D y G:")
for personaje in personajes_cdg:
    print(f"{personaje['nombre']} participó en {personaje['peliculas']} películas")
