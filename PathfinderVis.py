from os import curdir
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from queue import PriorityQueue
from collections import deque
import time
import threading

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
        self.button.config(bg='cornflower blue')

    def make_closed(self):
        self.button.config(bg='LightSkyBlue2')

    def enable(self):
        self.button.config(state=NORMAL)

    def disable(self):
        self.button.config(state=DISABLED)

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

# To reset the whole canvas state:


def Reset():
    global grid

    Node.start_point = None
    Node.end_point = None

    for row in grid:
        for node in row:
            node.reset()
            node.neighbors = []
            node.g = float('inf')
            node.h = 0
            node.f = float('inf')
            node.parent = None
            node.start = False
            node.end = False
            node.barrier = False
            node.enable()


def reconstruct_path(node, tickTime):
    current = node
    while current.start == False:
        parent = current.parent
            
        parent.make_path()
        root.update_idletasks()
        time.sleep(tickTime)

        current = parent

def breadth_first(grid, tickTime):
    
    start = grid[Node.start_point[1]][Node.start_point[0]]
    end = grid[Node.end_point[1]][Node.end_point[0]]
    
    open_set = deque()
    
    open_set.append(start)
    visited_hash = {start}
    
    while len(open_set) > 0:
        current = open_set.popleft()
        
        # found end?
        if current == end:
            reconstruct_path(end, tickTime)
            
            # draw end and start again
            end.make_end()
            start.make_start()
            return
        
        # if not end - consider all neighbors of current Node to choose next step
        for neighbor in current.neighbors:
            if neighbor not in visited_hash:
                neighbor.parent = current
                visited_hash.add(neighbor)
                open_set.append(neighbor)
                neighbor.make_open()
                
        # draw updated grid with new open_set        
        root.update_idletasks()
        time.sleep(tickTime)
        
        if current != start:
            current.make_closed()
            
    # didn't find path
    messagebox.showinfo("No Solution", "There was no solution")

    return False

def depth_first(grid, tickTime):
    start = grid[Node.start_point[1]][Node.start_point[0]]
    end = grid[Node.end_point[1]][Node.end_point[0]]

    open_set = deque([])
    open_set.append(start)
    visited_hash = {start}

    while len(open_set) > 0:
        current = open_set.pop()
        
        # found end?
        if current == end:
            reconstruct_path(end, tickTime)
            
            # draw end and start again
            end.make_end()
            start.make_start()
            return
        
    # if not end - consider all neighbors of current Node to choose next step
        if current not in visited_hash:
            visited_hash.add(current)

        for neighbor in current.neighbors:
            
            if neighbor not in visited_hash:
                neighbor.parent = current
                # visited_hash.add(neighbor)
                open_set.append(neighbor)
                neighbor.make_open()
                
        # draw updated grid with new open_set        
        root.update_idletasks()
        time.sleep(tickTime)
        
        if current != start:
            current.make_closed()

    return False

def djkstra(grid, tickTime):

    count = 0
    start = grid[Node.start_point[1]][Node.start_point[0]]
    end = grid[Node.end_point[1]][Node.end_point[0]]

    open_set = PriorityQueue()
    open_set_hash = {}

    open_set.put((0, count, start))

    start.g = 0

    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(end, tickTime)
            
            # draw end and start again
            end.make_end()
            start.make_start()
            
            # enable UI frame
            for child in UI_frame.winfo_children():
                child.configure(state='normal')
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = current.g + 1

            if temp_g_score < neighbor.g:
                neighbor.parent = current
                neighbor.g = temp_g_score

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((neighbor.g, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        root.update_idletasks()
        time.sleep(tickTime)
        
        if current != start:
            current.make_closed()

def a_star(grid, tickTime):

    count = 0
    start = grid[Node.start_point[1]][Node.start_point[0]]
    end = grid[Node.end_point[1]][Node.end_point[0]]
    
    # create open_set
    open_set = PriorityQueue()
    
    # add start in open_set with f_score = 0 and count as one item
    open_set.put((0, count, start))

    # put g_score for start to 0    
    start.g = 0
    
    # calculate f_score for start using heuristic function
    start.f = h(start, end)
    
    # create a dict to keep track of nodes in open_set, can't check PriorityQueue
    open_set_hash = {start}
    
    # if open_set is empty - all possible nodes are considered, path doesn't exist
    while not open_set.empty():
        
        # popping the Node with lowest f_score from open_set
        # if score the same, then whatever was inserted first - PriorityQueue
        # popping [2] - Node itself
        current = open_set.get()[2]
        # syncronise with dict
        open_set_hash.remove(current)
        
        # found end?
        if current == end:
            reconstruct_path(end, tickTime)
            
            # draw end and start again
            end.make_end()
            start.make_start()
            
            # enable UI frame
            for child in UI_frame.winfo_children():
                child.configure(state='normal')
            return True
        
        # if not end - consider all neighbors of current Node to choose next step
        for neighbor in current.neighbors:
            
            # calculate g_score for every neighbor
            temp_g_score = current.g + 1
            
            # if new path through this neighbor better
            if temp_g_score < neighbor.g:
                
                # update g_score for this Node and keep track of new best path
                neighbor.parent = current
                neighbor.g = temp_g_score
                neighbor.f = temp_g_score + h(neighbor, end)
                
                if neighbor not in open_set_hash:
                    
                    # count the step
                    count += 1
                    
                    # add neighbor in open_set for consideration
                    open_set.put((neighbor.f, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        # draw updated grid with new open_set        
        root.update_idletasks()
        time.sleep(tickTime)
        
        if current != start:
            current.make_closed()
            
    # didn't find path
    messagebox.showinfo("No Solution", "There was no solution" )

    return False

def StartAlgorithm():
    global grid
    if not grid:
        return
    if not Node.start_point or not Node.end_point:
        messagebox.showinfo(title="No start/end",
                            message="Place start and ending points")
        return

    # update neighbors based on current state
    for row in grid:
        for node in row:
            node.neighbors = []
            node.g = float('inf')
            node.h = 0
            node.f = float('inf')
            node.parent = None
            node.update_neighbors(grid)
            if node.clicked == False:
                node.reset()
            node.disable()  # disable Buttons

    # disable UI frame for running algortihm

    for row in grid:
        for node in row:
            node.enable()
    
    for child in UI_frame.winfo_children():
        child.configure(state="disable")

    # choose algorithm here...............
    threading.Thread(target=djkstra(grid, 0.05))
    # algortihm goes above................

    # enable all the disabled buttons and UI for next turn

    for child in UI_frame.winfo_children():
        child.configure(state="normal")


Button(UI_frame, text = "start", command=StartAlgorithm).grid(row = 1, column = 1)

grid = make_grid(WIDTH, ROWS)
root.mainloop()


