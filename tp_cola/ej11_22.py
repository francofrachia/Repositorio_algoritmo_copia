# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks

from cola import Queue

class Character:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def __str__(self):
        return f"{self.name} - {self.planet}"

# a. Mostrar los personajes del planeta Alderaan, Endor y Tatooine
def show_characters_by_planet(queue, planets):
    for character in queue.get_elements():
        if character.planet in planets:
            print(character)

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
def show_planet_of_characters(queue, character_names):
    for character in queue.get_elements():
        if character.name in character_names:
            print(f"{character.name} es de {character.planet}")

# c. Insertar un nuevo personaje antes del maestro Yoda
def insert_before_yoda(queue, new_character):
    temp_queue = Queue()
    inserted = False
    while queue.size() > 0:
        character = queue.attention()
        if character.name == "Yoda" and not inserted:
            temp_queue.arrive(new_character)
            inserted = True
        temp_queue.arrive(character)
    # Pasamos los elementos de la cola temporal a la original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

# d. Eliminar el personaje ubicado después de Jar Jar Binks
def remove_after_jar_jar(queue):
    temp_queue = Queue()
    remove_next = False
    while queue.size() > 0:
        character = queue.attention()
        if remove_next:
            remove_next = False  # Saltamos el siguiente personaje (después de Jar Jar Binks)
            continue
        temp_queue.arrive(character)
        if character.name == "Jar Jar Binks":
            remove_next = True
    # Pasamos los elementos de la cola temporal a la original
    while temp_queue.size() > 0:
        queue.arrive(temp_queue.attention())

# Creamos la cola de personajes
characters_queue = Queue()
characters_queue.arrive(Character("Luke Skywalker", "Tatooine"))
characters_queue.arrive(Character("Han Solo", "Corellia"))
characters_queue.arrive(Character("Leia Organa", "Alderaan"))
characters_queue.arrive(Character("Yoda", "Dagobah"))
characters_queue.arrive(Character("Jar Jar Binks", "Naboo"))
characters_queue.arrive(Character("Chewbacca", "Kashyyyk"))

# a. Mostrar personajes de Alderaan, Endor y Tatooine
print("Personajes de Alderaan, Endor y Tatooine:")
show_characters_by_planet(characters_queue, ["Alderaan", "Endor", "Tatooine"])

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
print("\nPlanetas de Luke Skywalker y Han Solo:")
show_planet_of_characters(characters_queue, ["Luke Skywalker", "Han Solo"])

# c. Insertar un nuevo personaje antes del maestro Yoda
print("\nInsertando a Obi-Wan Kenobi antes de Yoda:")
insert_before_yoda(characters_queue, Character("Obi-Wan Kenobi", "Stewjon"))
for character in characters_queue.get_elements():
    print(character)

# d. Eliminar el personaje después de Jar Jar Binks
print("\nEliminando el personaje después de Jar Jar Binks:")
remove_after_jar_jar(characters_queue)
for character in characters_queue.get_elements():
    print(character)

# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

from cola import Queue

class MCUCharacter:
    def __init__(self, character_name, superhero_name, gender):
        self.character_name = character_name
        self.superhero_name = superhero_name
        self.gender = gender

    def __str__(self):
        return f"{self.character_name}, {self.superhero_name}, {self.gender}"

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def find_character_by_superhero(queue, superhero_name):
    for character in queue.get_elements():
        if character.superhero_name == superhero_name:
            print(f"El personaje de {superhero_name} es {character.character_name}")
            return character.character_name
    print(f"No se encontró el personaje de {superhero_name}.")
    return None

# b. Mostrar los nombres de los superhéroes femeninos
def show_female_superheroes(queue):
    print("Superhéroes femeninos:")
    for character in queue.get_elements():
        if character.gender == "F":
            print(character.superhero_name)

# c. Mostrar los nombres de los personajes masculinos
def show_male_characters(queue):
    print("Personajes masculinos:")
    for character in queue.get_elements():
        if character.gender == "M":
            print(character.character_name)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def find_superhero_by_character(queue, character_name):
    for character in queue.get_elements():
        if character.character_name == character_name:
            print(f"El superhéroe de {character_name} es {character.superhero_name}")
            return character.superhero_name
    print(f"No se encontró el superhéroe de {character_name}.")
    return None

# e. Mostrar todos los datos de los personajes cuyos nombres comienzan con 'S'
def show_characters_starting_with_s(queue):
    print("Personajes o superhéroes cuyos nombres comienzan con 'S':")
    for character in queue.get_elements():
        if character.character_name.startswith("S") or character.superhero_name.startswith("S"):
            print(character)

# f. Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
def check_carol_danvers(queue):
    for character in queue.get_elements():
        if character.character_name == "Carol Danvers":
            print(f"Carol Danvers es {character.superhero_name}")
            return character.superhero_name
    print("Carol Danvers no se encuentra en la cola.")
    return None

# Creamos la cola de personajes MCU
mcu_queue = Queue()
mcu_queue.arrive(MCUCharacter("Tony Stark", "Iron Man", "M"))
mcu_queue.arrive(MCUCharacter("Steve Rogers", "Capitán América", "M"))
mcu_queue.arrive(MCUCharacter("Natasha Romanoff", "Black Widow", "F"))
mcu_queue.arrive(MCUCharacter("Carol Danvers", "Capitana Marvel", "F"))
mcu_queue.arrive(MCUCharacter("Scott Lang", "Ant-Man", "M"))
mcu_queue.arrive(MCUCharacter("Peter Parker", "Spider-Man", "M"))

# a. Determinar el nombre del personaje de Capitana Marvel
print("\na. Nombre del personaje de Capitana Marvel:")
find_character_by_superhero(mcu_queue, "Capitana Marvel")

# b. Mostrar los nombres de los superhéroes femeninos
print("\nb. Superhéroes femeninos:")
show_female_superheroes(mcu_queue)

# c. Mostrar los nombres de los personajes masculinos
print("\nc. Personajes masculinos:")
show_male_characters(mcu_queue)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
print("\nd. Superhéroe del personaje Scott Lang:")
find_superhero_by_character(mcu_queue, "Scott Lang")

# e. Mostrar todos los datos de los personajes cuyos nombres comienzan con 'S'
print("\ne. Personajes o superhéroes cuyos nombres comienzan con 'S':")
show_characters_starting_with_s(mcu_queue)

# f. Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
print("\nf. Carol Danvers en la cola:")
check_carol_danvers(mcu_queue)