from Classes.Node import Node

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

def depthSolveIterative(map, node):
    nodes = [node]
    while(len(nodes)):
        for index, node in enumerate(nodes):
            if node.victory(map):
                print("El estado ganador es:")
                print("Player:", node.playerPosition, "Boxes", node.boxesPositions)
                return node.findPath(map)
            newnodes = node.expandNode(map)
            del nodes[index]
            for index, nodo in enumerate(newnodes):
                nodes.insert(index, nodo)
    print("El nivel no tiene solucion")
