from Classes.Node import Node

def depthSolve(map, nodes):
    for node in nodes:
        if node.victory:
            return node.findPath
    for node in nodes:
        breadthSolve(map, node.expandNode(map))
