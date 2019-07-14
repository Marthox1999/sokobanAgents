""" 
Resolviendo Tableros de Sokoban

Integrantes:
Valeria Rivera Muñoz; Codigo 1626837
Juan Felipe Gil Londoño; Codigo 1626055
Mateo Gregory Jiemenz; 1629431
"""

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog


sokobanMap = None

def searchMap():
    global fileName

    fileName = tk.filedialog.askopenfilename()
    sokobanMap = open(fileName,"r")
    map = sokobanMap.readlines()
    print(map)
    map.remove('\n') #Erase the last entry ('cause is a newline)
    print(map)

    for i in range (0, len(map)):
        map[i]= map[i].replace('\n', '')
    print(map)

    witdh = len(map[0])
    height = 0
    print("witdh",witdh)

    for i in range(0, len(map)):
        if(("W" in map[i]) or ("0" in map[i])):
            height = height+1

    print("height", height)
    playerPosition = map[height].split(',')
    print("player position", playerPosition)
    numberOfBoxes = len(map)-1-height
    print("number of boxes", numberOfBoxes)

    boxes = [numberOfBoxes]
    j = 0
    for i in range(height+1, len(map)):
        print("j:",j+1)
        boxes[j] = map[i].split(',')
        print("boxes in:",boxes[j])
        j = j+1

    print("tamaño del mapa", len(map))
    print("number of boxes", boxes)


def main():
    root = tk.Tk()
    root.title("Sokoban")
    root.configure(bg="black")
    root.geometry("1000x600")
    root.resizable(0,0)

    searchMapButton = tk.Button(root, text="Search map", bg="gray30", fg="white", height=1, width=15, command=searchMap)
    searchMapButton.pack(padx=5, pady=5)

    root.mainloop()
    return 0


main()