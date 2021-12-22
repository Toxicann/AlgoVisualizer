from tkinter import *
from tkinter import ttk
from queue import PriorityQueue
from collections import deque
import random
import time

from PySimpleGUI.PySimpleGUI import T

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
canvas = Canvas(root, width=WIDTH, height=WIDTH, bg="white")
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

root.mainloop()
