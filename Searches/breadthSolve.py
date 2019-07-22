from Classes.Node import Node

def breadthSolveRevursive(map, nodes):
    for index, node in enumerate(nodes):
        if node.victory(map):
            print("El estado ganador es:")
            print("Player:", node.playerPosition, "Boxes", node.boxesPositions)
            return node.findPath(map)
        newnodes = node.expandNode(map)
        del nodes[index]
        for index, nodo in enumerate(newnodes):
            nodes.append(nodo)
        breadthSolveRevursive(map, nodes)
    print("El nivel no tiene solucion")

def breadthSolveIterative(map, node):
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
                nodes.append(nodo)
    print("El nivel no tiene solucion")
