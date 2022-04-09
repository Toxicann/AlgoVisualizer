from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PathfinderLogic import *


def init_pathfinder():
    WIDTH = 600

    root = Tk()
    root.title("Path Finding Visualizer")
    root.maxsize(1200, 613)
    root.config(bg="#19232d")
    selectedalg = StringVar()

    # Creating empty Canvas window (on left side for pathfinding window)
    canvas = Canvas(root, width=WIDTH, height=WIDTH, bg="gray4")
    canvas.pack(fill=Y, side=LEFT, padx=10, pady=5)

    # Creating Empty Frame for UI later on -  on right Side
    UI_frame = Frame(root, width=600, height=1200, bg="#19232d")
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

    myGui.getVal(canvas, root, rbutton_frame, button_frame,
                 selectedalg)  # sending vars to Pathfinder Logic
    init_grid()

    Radiobutton(rbutton_frame, text="Breadth First Algorithm", variable=selectedalg, value='breadth_first', justify="left", selectcolor="#19232d", activebackground="#19232d", activeforeground="white",
                bg="#19232d", fg="white", font=("Arial", 15)).grid(row=0, column=0, padx=5, pady=5, sticky="W")
    Radiobutton(rbutton_frame, text="Depth First Algorithm", variable=selectedalg, value='depth_first', justify="left", selectcolor="#19232d", activebackground="#19232d", activeforeground="white",
                bg="#19232d", fg="white", font=("Arial", 15)).grid(row=1, column=0, padx=5, pady=5, sticky="W")
    Radiobutton(rbutton_frame, text="Djkstra Algortihm", variable=selectedalg, value='djkstra', justify="left", selectcolor="#19232d", activebackground="#19232d", activeforeground="white",
                bg="#19232d", fg="white", font=("Arial", 15)).grid(row=0, column=1, padx=5, pady=5, sticky="W")
    Radiobutton(rbutton_frame, text="A Star Algorithm", variable=selectedalg, value='a_star', justify="left", selectcolor="#19232d", activebackground="#19232d", activeforeground="white",
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
