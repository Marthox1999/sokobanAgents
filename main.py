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
        busqueda = int(sys.argv[2])
        print(busqueda)
    except:
        sys.exit("por favor ingrese el path del nivel y el tipo de busqueda")

    map, playerPosition, boxes = searchMap(level)
    print("El estado inicial es:")
    print("Player:", playerPosition, "Boxes", boxes)

    node = Node(playerPosition, boxes, None, None)

    if (busqueda == 1):
        solution = depthSolveIterative(map, node)
        solutionString = ""
        for decision in solution:
            solutionString = solutionString + decision
        print (solutionString)
    elif(busqueda == 2):
        solution = breadthSolveIterative(map, node)
        solutionString = ""
        for decision in solution:
            solutionString = solutionString + decision
        print (solutionString)
    elif(busqueda == 3):
        solution = iterativeDepthSolveIterative(map, node)
        solutionString = ""
        for decision in solution:
            solutionString = solutionString + decision
        print (solutionString)
