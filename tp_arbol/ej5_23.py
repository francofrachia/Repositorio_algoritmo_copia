# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

from cola import Queue  # Usamos tu clase Queue
from arbol import BinaryTree  # Usamos tu clase BinaryTree

# a. Almacenar héroe o villano en cada nodo (ya está implementado al agregar nodos)

# b. Listar villanos ordenados alfabéticamente
def listar_villanos(arbol):
    villanos = []
    
    def __inorden_villanos(root):
        if root is not None:
            __inorden_villanos(root.left)
            if root.other_value.get('is_hero') is not True:
                villanos.append(root.value)
            __inorden_villanos(root.right)
    
    if arbol.root is not None:
        __inorden_villanos(arbol.root)
    
    return villanos

# c. Mostrar todos los superhéroes que empiezan con 'C'
def listar_superheroes_con_c(arbol):
    heroes_con_c = []
    
    def __inorden_superheroes_con_c(root):
        if root is not None:
            __inorden_superheroes_con_c(root.left)
            if root.other_value.get('is_hero') is True and root.value.startswith('C'):
                heroes_con_c.append(root.value)
            __inorden_superheroes_con_c(root.right)
    
    if arbol.root is not None:
        __inorden_superheroes_con_c(arbol.root)
    
    return heroes_con_c

# d. Contar cuántos superhéroes hay en el árbol (usamos la función contar_super_heroes de la clase BinaryTree)
def contar_superheroes(arbol):
    return arbol.contar_super_heroes()  # Ya implementado

# e. Modificar el nombre de Doctor Strange
def modificar_doctor_strange(arbol, nuevo_nombre):
    doctor = arbol.search("Doctor Strange")
    if doctor:
        doctor.value = nuevo_nombre
        print(f"Nombre modificado a: {nuevo_nombre}")
    else:
        print("Doctor Strange no se encuentra en el árbol.")

# f. Listar los superhéroes en orden descendente
def listar_superheroes_descendente(arbol):
    heroes_desc = []
    
    def __postorden_superheroes(root):
        if root is not None:
            __postorden_superheroes(root.right)
            if root.other_value.get('is_hero') is True:
                heroes_desc.append(root.value)
            __postorden_superheroes(root.left)
    
    if arbol.root is not None:
        __postorden_superheroes(arbol.root)
    
    return heroes_desc

# g. Generar un bosque (superhéroes y villanos)
def generar_bosque(arbol):
    arbol_heroes = BinaryTree()
    arbol_villanos = BinaryTree()

    def __separar_nodos(root):
        if root is not None:
            if root.other_value.get('is_hero') is True:
                arbol_heroes.insert_node(root.value, root.other_value)
            else:
                arbol_villanos.insert_node(root.value, root.other_value)
            __separar_nodos(root.left)
            __separar_nodos(root.right)
    
    if arbol.root is not None:
        __separar_nodos(arbol.root)
    
    return arbol_heroes, arbol_villanos

# Parte g-I: Contar nodos en cada árbol
def contar_nodos_arbol(arbol):
    return arbol.contar_super_heroes()

# Parte g-II: Barrido ordenado alfabéticamente de cada árbol
def barrido_ordenado_arbol(arbol):
    arbol.inorden()  # Ya tenemos un método inorden en BinaryTree

# Crear el árbol de personajes del MCU
arbol_mcu = BinaryTree()

# Insertamos algunos personajes del MCU
arbol_mcu.insert_node("Captain America", {'is_hero': True})
arbol_mcu.insert_node("Iron Man", {'is_hero': True})
arbol_mcu.insert_node("Thanos", {'is_hero': False})
arbol_mcu.insert_node("Doctor Strange", {'is_hero': True})
arbol_mcu.insert_node("Loki", {'is_hero': False})

# Listar villanos
villanos = listar_villanos(arbol_mcu)
print("Villanos ordenados alfabéticamente:", villanos)

# Superhéroes que empiezan con 'C'
heroes_con_c = listar_superheroes_con_c(arbol_mcu)
print("Superhéroes que empiezan con C:", heroes_con_c)

# Contar superhéroes
cantidad_superheroes = contar_superheroes(arbol_mcu)
print("Cantidad de superhéroes:", cantidad_superheroes)

# Modificar Doctor Strange
modificar_doctor_strange(arbol_mcu, "Dr. Strange")

# Listar superhéroes en orden descendente
heroes_desc = listar_superheroes_descendente(arbol_mcu)
print("Superhéroes en orden descendente:", heroes_desc)

# Generar un bosque
arbol_heroes, arbol_villanos = generar_bosque(arbol_mcu)

# Contar nodos en cada árbol
print("Cantidad de nodos en el árbol de superhéroes:", contar_nodos_arbol(arbol_heroes))
print("Cantidad de nodos en el árbol de villanos:", contar_nodos_arbol(arbol_villanos))

# Barrido ordenado alfabéticamente
print("Superhéroes ordenados:")
barrido_ordenado_arbol(arbol_heroes)

print("Villanos ordenados:")
barrido_ordenado_arbol(arbol_villanos)


# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from cola import Queue
from arbol import BinaryTree

# Definición de la clase para la criatura
class Creature:
    def __init__(self, name, defeated_by=None, description=None, captured_by=None):
        self.name = name
        self.defeated_by = defeated_by  # Quien derrotó a la criatura
        self.description = description  # Descripción breve de la criatura
        self.captured_by = captured_by  # Quién capturó a la criatura

# Árbol de criaturas mitológicas
creatures_tree = BinaryTree()

# Cargar criaturas en el árbol
creatures = [
    ("Ceto", None), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"),
    ("Dino", None), ("Pefredo", None), ("Enio", None), ("Escila", None),
    ("Caribdis", None), ("Euríale", None), ("Esteno", None), ("Medusa", "Perseo"),
    ("Ladón", "Heracles"), ("Águila del Cáucaso", None), ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"), ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"), ("Dragón de la Cólquida", None), ("Cerbero", None),
    ("Toro de Creta", "Teseo"), ("Cierva de Cerinea", "Heracles"), ("Jabalí de Erimanto", "Heracles")
]

# Insertamos las criaturas en el árbol
for name, defeated_by in creatures:
    creatures_tree.insert_node(name, {"defeated_by": defeated_by})

# Consultas

# a. Listado inorden de las criaturas y quienes las derrotaron
print("Listado Inorden de las criaturas y quién las derrotó:")
creatures_tree.inorden()

# b. Cargar descripción sobre cada criatura
cerbero = creatures_tree.search("Cerbero")
if cerbero:
    cerbero.other_value["description"] = "Un perro monstruoso con tres cabezas"
medusa = creatures_tree.search("Medusa")
if medusa:
    medusa.other_value["description"] = "Una de las tres gorgonas, derrotada por Perseo"

# c. Mostrar información de la criatura Talos
talos = creatures_tree.search("Talos")
if talos:
    print(f"Talos: {talos.value}, Derrotado por: {talos.other_value.get('defeated_by')}")

# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
heroes_count = {}
def count_defeats(root):
    if root is not None:
        defeated_by = root.other_value.get("defeated_by")
        if defeated_by:
            if defeated_by in heroes_count:
                heroes_count[defeated_by] += 1
            else:
                heroes_count[defeated_by] = 1
        count_defeats(root.left)
        count_defeats(root.right)

count_defeats(creatures_tree.root)
top_heroes = sorted(heroes_count.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 héroes que derrotaron más criaturas:", top_heroes)

# e. Listar las criaturas derrotadas por Heracles
print("Criaturas derrotadas por Heracles:")
defeated_by_heracles = []
def list_defeated_by_heracles(root):
    if root is not None:
        if root.other_value.get("defeated_by") == "Heracles":
            defeated_by_heracles.append(root.value)
        list_defeated_by_heracles(root.left)
        list_defeated_by_heracles(root.right)

list_defeated_by_heracles(creatures_tree.root)
print(defeated_by_heracles)

# f. Listar criaturas que no han sido derrotadas
print("Criaturas no derrotadas:")
undefeated_creatures = []
def list_undefeated(root):
    if root is not None:
        if root.other_value.get("defeated_by") is None:
            undefeated_creatures.append(root.value)
        list_undefeated(root.left)
        list_undefeated(root.right)

list_undefeated(creatures_tree.root)
print(undefeated_creatures)

# g. Actualizar capturas realizadas por Heracles
creatures_tree.search("Cerbero").other_value["captured_by"] = "Heracles"
creatures_tree.search("Toro de Creta").other_value["captured_by"] = "Heracles"
creatures_tree.search("Cierva de Cerinea").other_value["captured_by"] = "Heracles"
creatures_tree.search("Jabalí de Erimanto").other_value["captured_by"] = "Heracles"

# h. Modificar las criaturas capturadas por Heracles
criaturas_heracles = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]

for criatura in criaturas_heracles:
    nodo = creatures_tree.search(criatura)
    if nodo:
        nodo.other_value["captured_by"] = "Heracles"
    else:
        print(f"No se encontró la criatura {criatura} en el árbol.")

# i. Eliminar al Basilisco y las Sirenas
creatures_tree.delete_node("Basilisco")
creatures_tree.delete_node("Sirenas")

# j. Modificar nodo de Aves del Estínfalo, agregar que Heracles derrotó varias
aves_estinfalo = creatures_tree.search("Aves del Estínfalo")
if aves_estinfalo:
    aves_estinfalo.other_value["defeated_by"] = "Heracles (varias)"

# k. Modificar el nombre de la criatura Ladón a Dragón Ladón
ladon = creatures_tree.search("Ladón")
if ladon:
    ladon.value = "Dragón Ladón"

# l. Listado por nivel del árbol
print("Listado por nivel:")
creatures_tree.by_level()

# m. Mostrar criaturas capturadas por Heracles
print("Criaturas capturadas por Heracles:")
captured_by_heracles = []
def list_captured_by_heracles(root):
    if root is not None:
        if root.other_value.get("captured_by") == "Heracles":
            captured_by_heracles.append(root.value)
        list_captured_by_heracles(root.left)
        list_captured_by_heracles(root.right)

list_captured_by_heracles(creatures_tree.root)
print(captured_by_heracles)