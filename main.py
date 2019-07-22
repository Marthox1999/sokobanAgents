"""
Resolviendo Tableros de Sokoban

Integrantes:
Valeria Rivera Muñoz; Codigo 1626837
Juan Felipe Gil Londoño; Codigo 1626055
Mateo Gregory Jiemenz; 1629431
"""
import sys
from Classes.Node import Node
from LoadingFiles.LoadMap import searchMap
from Searches.breadthSolve import *
from Searches.depthSolve import *
from Searches.iterativeDepthSolve import *

if __name__ == '__main__':
    try:
        level = sys.argv[1]
        print(level)
    except:
        sys.exit("por favor ingrese el correcto path de un nivel")

    map, playerPosition, boxes = searchMap(level)

    node = Node(playerPosition, boxes, None, None)

    solution = depthSolveIterative(map, node)
    solutionString = ""
    for decision in solution:
        solutionString = solutionString + decision
    print (solutionString)

    solution = breadthSolveIterative(map, node)
    solutionString = ""
    for decision in solution:
        solutionString = solutionString + decision
    print (solutionString)
    
    solution = iterativeDepthSolveIterative(map, node)
    solutionString = ""
    for decision in solution:
        solutionString = solutionString + decision
    print (solutionString)
