from pila import Stack

def interseccion(pila1, pila2):
    conjunto1 = set()
    conjunto2 = set()
    
    while pila1.size() > 0:
        conjunto1.add(pila1.pop())
    
    while pila2.size() > 0:
        conjunto2.add(pila2.pop())
    
    conjunto_interseccion = conjunto1.intersection(conjunto2)
    
    pila_interseccion = Stack()
    for item in conjunto_interseccion:
        pila_interseccion.push(item)
    
    return pila_interseccion

pila1 = Stack()
pila2 = Stack()

personajes_episodio_V = ["Luke Skywalker", "Darth Vader", "Han Solo", "Leia Organa", "Chewbacca"]

personajes_episodio_VII = ["Han Solo", "Leia Organa", "Rey", "Finn", "Kylo Ren", "Chewbacca"]

for personaje in personajes_episodio_V:
    pila1.push(personaje)

for personaje in personajes_episodio_VII:
    pila2.push(personaje)

pila_interseccion = interseccion(pila1, pila2)

print("Intersección de personajes en ambos episodios:")
while pila_interseccion.size() > 0:
    print(pila_interseccion.pop())
