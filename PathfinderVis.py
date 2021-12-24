from tkinter import *
from tkinter import ttk
from queue import PriorityQueue
from collections import deque
import random
import time

root = Tk()
root.title("Path Finding Visualizer")
root.maxsize(900, 900)
root.config(bg="#19232d")

# Global Variables
selected_alg = StringVar()
WIDTH = 500
ROWS = 25
grid = []

# Creating Canvas (on left side for acutal window)
canvas = Canvas(root, width=WIDTH, height=WIDTH, bg="gray4")
canvas.pack(fill=Y, side=LEFT, padx=10, pady=5)

# Creating Frame for UI later on -  on right Side
UI_frame = Frame(root, width=600, height=200, bg="#19232d")
UI_frame.pack(side=RIGHT, padx=10, pady=5)


class Node:

    start_point = None
    end_point = None

    __slots__ = ['button', 'row', 'col', 'width', 'neighbors', 'g', 'h', 'f',
                 'parent', 'start', 'end', 'barrier', 'clicked', 'total_rows']

    def __init__(self, row, col, width, offset, total_rows):
        self.button = Button(canvas, command=lambda a=row, b=col: self.click(a, b),
                             bg='white', bd=2, relief=GROOVE)

        self.row = row
        self.col = col
        self.width = width

        self.button.place(x=row * width + offset, y=col *
                          width + offset, height=width, width=width)

        self.neighbors = []
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.parent = None
        self.start = False
        self.end = False
        self.barrier = False
        self.clicked = False
        self.total_rows = total_rows

    def make_start(self):
        self.button.config(bg="DarkOrange2")
        self.start = True
        self.clicked = True
        Node.start_point = (self.col, self.row)

    def make_end(self):
        self.button.config(bg="lime green")
        self.end = True
        self.clicked = True
        Node.end_point = (self.col, self.row)

    def make_barrier(self):
        self.button.config(bg="black")
        self.barrier = True
        self.clicked = True
        
    def reset(self):
        self.button.config(bg="white")
        self.clicked = False
    
    def make_path(self):
        self.button.config(bg="gold")
    
    def make_to_visit(self):
        self.button.config(bg="purple")

    def make_open(self):
        self.buttonn.config(bg='cornflower blue')

    def make_closed(self):
        self.button.config(bg='LightSkyBlue2')

def make_grid(width, rows):
    gap = width // rows
    offset = 2
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, offset, rows)
            grid[i].append(node)
    return grid

grid = make_grid(WIDTH, ROWS)

root.mainloop()
