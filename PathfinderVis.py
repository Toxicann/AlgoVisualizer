from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PathfinderLogic import *


def init_pathfinder():
    WIDTH = 600

    root = Tk()
    root.title("Path Finding Visualizer")
    root.maxsize(1700, 613)
    root.config(bg="#19232d")
    selectedalg = StringVar()

    # Creating empty Canvas window (on left side for pathfinding window)
    algo_frame = Frame(root, width=350, height=600, bg="#19232d")
    algo_frame.pack(side=LEFT, padx=10, pady=5)

    canvas = Canvas(root, width=WIDTH, height=WIDTH, bg="gray4")
    canvas.pack(fill=Y, side=LEFT, padx=10, pady=5)

    # Creating Empty Frame for UI later on -  on right Side
    UI_frame = Frame(root, width=1200, height=600, bg="#19232d")
    UI_frame.pack(side=RIGHT, padx=10, pady=5)

    # GUI WINDOW BUTTONS/ RADIOBUTTONS and other things below here:

    Label(UI_frame, text="PathFinding Visualizer", bg="#19232d", fg="white", font=(
        "Arial", 32), justify=CENTER).grid(row=0, column=0, padx=10, pady=5)
    Label(UI_frame, text="Generate Path From Your Desired Algorithm", bg="#19232d",
          fg="white", font=("Arial", 16), justify=CENTER).grid(row=1, column=0, padx=10, pady=5)

    rbutton_frame = Frame(UI_frame, bg="#19232d", bd=1, relief=SUNKEN)
    rbutton_frame.grid(row=2, column=0, padx=10, pady=10)

    button_frame = Frame(UI_frame, bg="#19232d")
    button_frame.grid(row=3, column=0, padx=10, pady=5)

    #Color Labels###############################
    Label(algo_frame, text="Color representation", bg="#19232d", fg="white", font=(
        "Arial", 28), justify=CENTER).grid(row=0, column=0)
    Label(algo_frame, text="Start_Node => Forest Green", justify=LEFT, bg="#32414b", fg="forest green", width=30, relief=SUNKEN, font=(
        "Arial", 12)).grid(row=1, column=0)
    Label(algo_frame, text="End_Node => Dark Orange", justify=LEFT, bg="#32414b", fg="DarkOrange2", width=30, relief=SUNKEN, font=(
        "Arial", 12)).grid(row=2, column=0)
    Label(algo_frame, text="Barrier_Node => Black", justify=LEFT, bg="#32414b", fg="black", width=30, relief=SUNKEN, font=(
        "Arial", 12)).grid(row=3, column=0)
    Label(algo_frame, text="Path_Node => Gold", justify=LEFT, bg="#32414b", fg="gold", width=30, relief=SUNKEN, font=(
        "Arial", 12)).grid(row=4, column=0)
    Label(algo_frame, text="Visited_Node => Sky Blue", justify=LEFT, bg="#32414b", fg="LightSkyBlue2", width=30, relief=SUNKEN, font=(
        "Arial", 12)).grid(row=5, column=0)
    Label(algo_frame, text="Node_To_Visit => Yellow Green", justify=LEFT, bg="#32414b", fg="yellow green", width=30, relief=SUNKEN, font=(
        "Arial", 12)).grid(row=6, column=0)
    ########SPACE#######
    Label(algo_frame, text="", justify=LEFT, bg="#19232d", width=30, font=(
        "Arial", 20)).grid(row=7, column=0)
    ##########ALGORITHM DESC HERE###################
    ALGO_NAME = Label(algo_frame, text="", bg="#19232d", fg="white", font=(
        "Arial", 20), justify=LEFT)
    ALGO_NAME.grid(row=8, column=0)
    ALGO_DESC = Message(algo_frame, text="", bg="#19232d", fg="white", font=(
        "Arial", 14), justify=LEFT)
    ALGO_DESC.grid(row=9, column=0)
    TIMECMPLX = Label(algo_frame, text="", bg="#19232d", fg="white", font=(
        "Arial", 12), justify=LEFT)
    TIMECMPLX.grid(row=10, column=0)

    myGui.getVal(canvas, root, rbutton_frame, button_frame,
                 selectedalg)  # sending vars to Pathfinder Logic
    init_grid()

    def Refresh_Labels():
        if selectedalg.get() == "breadth_first":
            ALGO_NAME.configure(text="Breadth First:")
            ALGO_DESC.configure(
                text="Breadth-first search (BFS) is an algorithm that starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.")
            TIMECMPLX.configure(
                text="Time Complexity => O(V + E)")
        elif selectedalg.get() == "depth_first":
            ALGO_NAME.configure(text="Depth First")
            ALGO_DESC.configure(text="Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node or selected node in this case and explores as far as possible along each branch before backtracking.")
            TIMECMPLX.configure(
                text="Time Complexity => O(V + E)")
        elif selectedalg.get() == "djkstra":
            ALGO_NAME.configure(text="Djkstra")
            ALGO_DESC.configure(
                text="Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph. Dijkstra's algorithm is similar to BFS as it calculates the same thing in weighted graphs.")
            TIMECMPLX.configure(
                text="Time Complexity => O(E Log V)")
        elif selectedalg.get() == "a_star":
            ALGO_NAME.configure(text="A Star")
            ALGO_DESC.configure(text=" A-star algorithm (A*) is one of the most successful search algorithms to find the shortest path between nodes or graphs. It is an informed search algorithm, as it uses information about path cost and also uses heuristics to find the solution.")
            TIMECMPLX.configure(
                text="Time Complexity => O(E)")

    Radiobutton(rbutton_frame, text="Breadth First Algorithm", variable=selectedalg, value='breadth_first', command=Refresh_Labels, justify="left", selectcolor="#19232d", activebackground="#19232d", activeforeground="white",
                bg="#19232d", fg="white", font=("Arial", 15)).grid(row=0, column=0, padx=5, pady=5, sticky="W")
    Radiobutton(rbutton_frame, text="Depth First Algorithm", variable=selectedalg, value='depth_first', command=Refresh_Labels, justify="left", selectcolor="#19232d", activebackground="#19232d", activeforeground="white",
                bg="#19232d", fg="white", font=("Arial", 15)).grid(row=1, column=0, padx=5, pady=5, sticky="W")
    Radiobutton(rbutton_frame, text="Djkstra Algortihm", variable=selectedalg, value='djkstra', command=Refresh_Labels, justify="left", selectcolor="#19232d", activebackground="#19232d", activeforeground="white",
                bg="#19232d", fg="white", font=("Arial", 15)).grid(row=0, column=1, padx=5, pady=5, sticky="W")
    Radiobutton(rbutton_frame, text="A Star Algorithm", variable=selectedalg, value='a_star', command=Refresh_Labels, justify="left", selectcolor="#19232d", activebackground="#19232d", activeforeground="white",
                bg="#19232d", fg="white", font=("Arial", 15)).grid(row=1, column=1, padx=5, pady=5, sticky="W")

    Button(button_frame, text="Start", bg="#32414b", fg="white",
           font=("Arial", 20), command=thread_startalgo).pack(side=LEFT, padx=10, pady=5)
    Button(button_frame, text="Reset", bg="#32414b", fg="white",
           font=("Arial", 20), command=Reset).pack(side=RIGHT, padx=10, pady=5)
    Button(button_frame, text="Maze 1", bg="#32414b", fg="white",
           font=("Arial", 16), command=Node.generate_prebuilt_maze).pack(side="top", padx=10, pady=5)
    Button(button_frame, text="Maze 2", bg="#32414b", fg="white",
           font=("Arial", 16), command=Node.generate_prebuilt_maze1).pack(side="bottom", padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    init_pathfinder()
