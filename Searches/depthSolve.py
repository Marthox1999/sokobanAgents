from Classes.Node import Node
import time

def depthSolveRecursive(map, nodes):
    for index, node in enumerate(nodes):
        if node.victory(map):
            print("Gane", node.victory(map))
            print("Player:", node.playerPosition, "Boxes", node.boxesPositions)
            return node.findPath(map)

        newnodes = node.expandNode(map)
        del nodes[index]
        for index, nodo in enumerate(newnodes):
            nodes.insert(index, nodo)
        depthSolveRecursive(map, nodes)

def depthSolveIterative(map, node, Max_tree_depth):
    nodes = [node]
    while(nodes):
        nodo = nodes[0]
        del nodes[0]
        if nodo.victory(map):
            return nodo.findPath(map)
        if(nodo.depth < Max_tree_depth):
            newnodes = nodo.expandNode(map)
            for index, nodo in enumerate(newnodes):
                nodes.insert(index, nodo)
    print("El nivel no tiene solucion")
