from os import curdir
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from queue import PriorityQueue
from collections import deque
import time
import threading

from PathfinderLogic import *

def init_pathfinder():
    WIDTH = 500

    root = Tk()
    root.title("Path Finding Visualizer")
    root.maxsize(900, 900)
    root.config(bg="#19232d")

    # Global Variables
    selected_alg = StringVar()

    # Creating empty Canvas window (on left side for pathfinding window)
    canvas = Canvas(root, width=WIDTH, height=WIDTH, bg="gray4")
    canvas.pack(fill=Y, side=LEFT, padx=10, pady=5)

    # Creating Empty Frame for UI later on -  on right Side
    UI_frame = Frame(root, width=600, height=200, bg="#19232d")
    UI_frame.pack(side=RIGHT, padx=10, pady=5)

    myGui.getVal(canvas, root, UI_frame) #sending vars to Pathfinder Logic
    init_grid()
    
    Button(UI_frame, text = "start", command=StartAlgorithm).grid(row = 1, column = 1)

    root.mainloop()

if __name__ == "__main__":
    init_pathfinder()

