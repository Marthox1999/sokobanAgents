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

def iterativeDepthSolveIterative(map, node, Max_tree_depth):
    initNode = node
    for i in range (Max_tree_depth + 1):
        nodes = [node]
        while(nodes):
            nodo = nodes[0]
            del nodes[0]
            if nodo.victory(map):
                return nodo.findPath(map)
            if(nodo.depth < i):
                newnodes = nodo.expandNode(map)
                for index, nodo in enumerate(newnodes):
                    nodes.insert(index, nodo)
    print("El nivel no tiene solucion")
