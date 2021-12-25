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

# Creating empty Canvas window (on left side for pathfinding window)
canvas = Canvas(root, width=WIDTH, height=WIDTH, bg="gray4")
canvas.pack(fill=Y, side=LEFT, padx=10, pady=5)

# Creating Empty Frame for UI later on -  on right Side
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

    def enable(self):
        self.button.config(state = NORMAL)
    
    def disable(self):
        self.button.config(state = DISABLED)

    def click(self, row, col):
        if self.clicked == False:
            if not Node.start_point:
                self.make_start()
            elif not Node.end_point:
                self.make_end()
            else:
                self.make_barrier()
        else:
            self.reset()
            if self.start == True:
                self.start = False
                Node.start_point = None
            elif self.end == True:
                self.end = False
                Node.end_point = None
            else:
                self.barrier = False

    def update_neighbors(self, grid):
        self.neighbors = []

        # check neighbors a row down - if not outside grid and not barrier
        if self.row < (self.total_rows - 1) and not grid[self.row + 1][self.col].barrier:
            # add this node to neighbor list
            self.neighbors.append(grid[self.row + 1][self.col])

        # check neighbors a row up - if not outside grid and not barrier
        if self.row > 0 and not grid[self.row - 1][self.col].barrier:
            self.neighbors.append(grid[self.row - 1][self.col])

        # check neighbors a col right:
        if self.col < (self.total_rows - 1) and not grid[self.row][self.col + 1].barrier:
            self.neighbors.append(grid[self.row][self.col + 1])

        # check neighbors a col left:
        if self.col > 0 and not grid[self.row][self.col - 1].barrier:
            self.neighbors.append(grid[self.row][self.col - 1])


# to make grid in our canvas window
def make_grid(width, rows):
    gap = width // rows
    offset = 2
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, offset, rows)
            grid[i].append(node)
    return grid


def h(a, b):
    # heuristic function - manhatten distance
    return abs(a.row - b.row) + abs(a.col - b.col)




# inatilize grid
grid = make_grid(WIDTH, ROWS)

root.mainloop()
