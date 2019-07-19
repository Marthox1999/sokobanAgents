"""
Resolviendo Tableros de Sokoban

Integrantes:
Valeria Rivera Muñoz; Codigo 1626837
Juan Felipe Gil Londoño; Codigo 1626055
Mateo Gregory Jiemenz; 1629431
"""
from Classes.Node import Node
from LoadingFiles.LoadMap import searchMap
from Functions.Functions import *

if __name__ == '__main__':
    map, playerPosition, boxes = searchMap()

    print("player position", playerPosition)
    print("boxes in map", boxes)
    print("1 - profunidad \n 2 - amplitud \n 3 - profunidad iterativa")
    busqueda = int(input("por favor ingrese que tipo de busqueda desea hacer:"))

    node = Node(playerPosition, boxes, None, None)
    print("posicion del jugador en el nodo: ", node.playerPosition)
    print("posicion de las cajas en el nodo: ", node.boxesPositions)

    newnode = node.expandNode(map)
    for index, nodo in enumerate(newnode):
        print("\n En el movimiento numero ", index)
        print("posicion del jugador en el nodo: ", nodo.playerPosition)
        print("posicion de las cajas en el nodo: ", nodo.boxesPositions)

    return 0
