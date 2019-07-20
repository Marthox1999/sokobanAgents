from Classes.Node import Node
import time

def depthSolveRecursive(map, nodes):
    for node in nodes:
        if node.victory:
            return node.findPath
    for node in nodes:
        depthSolveRecursive(map, node.expandNode(map))

def depthSolveIterative(map, node):
    nodes = [node]
    while(len(nodes)):
        print("\n")
        for index, node in enumerate(nodes):
            if node.victory(map):
                print("Gane")
                return node.findPath()
            newnodes = node.expandNode(map)
            del nodes[index]
            for index, nodo in enumerate(newnodes):
                nodes.insert(index, nodo)
            print("Player: ",node.playerPosition,"Boxes: ", node.boxesPositions)
