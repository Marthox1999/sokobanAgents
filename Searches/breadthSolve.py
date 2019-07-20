from Classes.Node import Node

def breadthSolveIterative(map, nodes):
    for node in nodes:
        if node.victory:
            return node.findPath
        nodes.append(node.expandNode(map))
