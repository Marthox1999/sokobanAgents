from Classes.Node import Node

def iterativeDepthSolveRecursiveMain(map,nodes, iteration):
    result = iterativeDepthSolveRecursive(map, nodes, depth) == False
    if(result == False):
        iteration = iteration + 1
        iterativeDepthSolveRecursiveMain(map,nodes, iteration)
    else:
        return result
    return 0

def iterativeDepthSolveRecursive(map, nodes, depth):
    for index, node in enumerate(nodes):
        if (node.findDepth() > depth):
            return false
        if (node.victory(map)):
            print("El estado ganador es:")
            print("Player:", node.playerPosition, "Boxes", node.boxesPositions)
            return node.findPath(map)
        newnodes = node.expandNode(map)
        del nodes[index]
        for index, nodo in enumerate(newnodes):
            nodes.insert(index, nodo)
        iterativeDepthSolveRecursive(map, nodes)

def iterativeDepthSolveIterative(map, node):
    nodes = [node]
    i = 0
    while (len(nodes)):
        i = i+1
        continueIteration = False
        while(len(nodes) or continueIteration):
            for index, node in enumerate(nodes):
                if (node.findDepth() > i):
                    continueIteration = True
                if node.victory(map):
                    print("El estado ganador es:")
                    print("Player:", node.playerPosition, "Boxes", node.boxesPositions)
                    return node.findPath(map)
                newnodes = node.expandNode(map)
                del nodes[index]
                for index, nodo in enumerate(newnodes):
                    nodes.insert(index, nodo)
    print("El nivel no tiene solucion")
