class HeapMin():
    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.float(len(self.elements) - 1)

    def remove(self):
        if len(self.elements) > 0:
            self.interchange(0, len(self.elements) - 1)
            value = self.elements.pop()
            self.sink(0)
            return value
        else:
            return None

    def interchange(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def float(self, index):
        father = (index - 1) // 2
        while index > 0 and self.elements[index][0] < self.elements[father][0]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index):
        left_child = (index * 2) + 1
        control = True
        while control and left_child < len(self.elements):
            right_child = (index * 2) + 2
            min_index = left_child
            if right_child < len(self.elements):
                if self.elements[right_child][0] < self.elements[left_child][0]:
                    min_index = right_child
            if self.elements[index][0] > self.elements[min_index][0]:
                self.interchange(index, min_index)
                index = min_index
                left_child = (index * 2) + 1
            else:
                control = False

    def arrive(self, value, priority):
        self.add([priority, value])

    def atention(self):
        return self.remove()

class Pedido:
    def __init__(self, general, planeta, descripcion):
        self.general = general
        self.planeta = planeta
        self.descripcion = descripcion

    def __str__(self):
        return f"General: {self.general}, Planeta: {self.planeta}, Descripción: {self.descripcion}"

# Función para determinar la prioridad
def determinar_prioridad(pedido):
    if pedido.general == "Gran Inquisidor" or pedido.planeta == "Lothal" or "Hera Syndulla" in pedido.descripcion:
        return 1  # Prioridad alta
    elif pedido.general == "Agente Kallus" or "Destructor Estelar" in pedido.descripcion or "AT-AT" in pedido.descripcion:
        return 2  # Prioridad media
    else:
        return 3  # Prioridad baja

# Sistema de atención a pedidos
def main():
    cola_pedidos = HeapMin()
    bitacora = []

    # Simulamos algunos pedidos
    pedidos = [
        Pedido("Gran Inquisidor", "Lothal", "Necesito un informe sobre Hera Syndulla."),
        Pedido("Agente Kallus", "Coruscant", "Requiere apoyo con el Destructor Estelar."),
        Pedido("General Veers", "Hoth", "Situación crítica en la base."),
        Pedido("General Tarkin", "Scarif", "Requiere refuerzos."),
        Pedido("Agente Kallus", "Endor", "AT-AT en posición de combate."),
    ]

    # Agregar pedidos a la cola
    for pedido in pedidos:
        prioridad = determinar_prioridad(pedido)
        cola_pedidos.arrive(pedido, prioridad)

    # Atender los pedidos
    while len(cola_pedidos.elements) > 0:
        pedido_atendido = cola_pedidos.atention()
        bitacora.append(pedido_atendido[1])  # Agregamos a la bitácora
        print(f"Atendiendo pedido: {pedido_atendido[1]}")

    # Mostrar la bitácora
    print("\nBitácora de pedidos atendidos:")
    for p in bitacora:
        print(p)

if __name__ == "__main__":
    main()