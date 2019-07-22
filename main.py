"""
Resolviendo Tableros de Sokoban

Integrantes:
Valeria Rivera Muñoz; Codigo 1626837
Juan Felipe Gil Londoño; Codigo 1626055
Mateo Gregory Jiemenz; 1629431
"""
from Classes.Node import Node
from LoadingFiles.LoadMap import searchMap
from Searches.breadthSolve import *
from Searches.depthSolve import *
from Searches.iterativeDepthSolve import *

if __name__ == '__main__':

    map, playerPosition, boxes = searchMap()
    Max_tree_depth = 64
    node = Node(playerPosition, boxes, None, None, 0)

    breadthSolution = breadthSolveIterative(map, node, Max_tree_depth)
    breadthSolutionString = ""
    for decision in breadthSolution:
        breadthSolutionString = breadthSolutionString + decision
    print (breadthSolutionString)

    depthSolution = depthSolveIterative(map, node, Max_tree_depth)
    depthSolutionString = ""
    for decision in depthSolution:
        depthSolutionString = depthSolutionString + decision
    print (depthSolutionString)

    iterativeDepthSolution = iterativeDepthSolveIterative(map, node, Max_tree_depth)
    iterativeDepthSolutionString = ""
    for decision in iterativeDepthSolution:
        iterativeDepthSolutionString = iterativeDepthSolutionString + decision
    print (iterativeDepthSolutionString)
