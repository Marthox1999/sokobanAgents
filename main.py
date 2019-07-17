"""
Resolviendo Tableros de Sokoban

Integrantes:
Valeria Rivera Muñoz; Codigo 1626837
Juan Felipe Gil Londoño; Codigo 1626055
Mateo Gregory Jiemenz; 1629431
"""

from LoadingFiles.LoadMap import searchMap

def main():
    map, playerPosition, boxes = searchMap()
    print("1 - profunidad \n 2 - amplitud \n 3 - profunidad iterativa")
    busqueda = int(input("por favor ingrese que tipo de busqueda desea hacer:"))
    return 0

main()
