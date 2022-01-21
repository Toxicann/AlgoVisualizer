import sortingAlgorithm
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from matplotlib.ticker import NullFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')


class TrackedArray():

    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []
        self.full_copies = []

    def track(self, key, access_type):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))

    def GetActivity(self, idx=None):
        if isinstance(idx, type(None)):
            return [(i, op) for (i, op) in zip(self.indices, self.access_type)]
        else:
            return (self.indices[idx], self.access_type[idx])

    def __getitem__(self, key):
        self.track(key, "get")
        return self.arr.__getitem__(key)

    def __setitem__(self, key, value):
        self.arr.__setitem__(key, value)
        self.track(key, "set")

    def __len__(self):
        return self.arr.__len__()


class myVals:
    N = 30
    sortVal = 4

    @classmethod
    def getVal(cls, value1, value2):
        cls.N = value1
        cls.sortVal = value2
        # print(cls.N, cls.sortVal)


def run():
    FPS = 60.0
    arr = np.round(np.linspace(0, 1000, int(myVals.N)), 0)
    np.random.shuffle(arr)
    # print(myVals.N)
    arr = TrackedArray(arr)

    ##################################
    if myVals.sortVal == 1:
        sorter = "Insertion"

        t0 = time.perf_counter()  # initial time
        sortingAlgorithm.insertionSort(arr)
        dt = time.perf_counter() - t0  # current - initial time = exec time
    #####################################
    elif myVals.sortVal == 2:
        sorter = "Bubble"

        t0 = time.perf_counter()
        sortingAlgorithm.bubbleSort(arr)
        dt = time.perf_counter() - t0
    ####################################

    elif myVals.sortVal == 3:
        sorter = "Selection"

        t0 = time.perf_counter()
        sortingAlgorithm.selectionSort(arr, len(arr))
        dt = time.perf_counter() - t0
    #####################################
    elif myVals.sortVal == 4:
        sorter = "Quick"

        t0 = time.perf_counter()
        sortingAlgorithm.quickSort(arr, 0, len(arr) - 1)
        dt = time.perf_counter() - t0
    #####################################

    print(f"-------{sorter} sort-----------")
    print(f"Array sorted in {dt*1E3:.1f} ms")

    fig, ax = plt.subplots(figsize=(7.5, 15))
    container = ax.bar(np.arange(0, len(arr), 1),
                       arr.full_copies[0], align="edge", width=0.8)
    ax.set_xlim([0, myVals.N])
    ax.set(xlabel="Index", ylabel="Value", title=f"{sorter} sort")
    txt = ax.text(0, 1000, "")

    def update(frame):
        txt.set_text(f"Accesses = {frame}")
        for (rectangle, height) in zip(container.patches, arr.full_copies[frame]):
            rectangle.set_height(height)
            rectangle.set_color("#1f77b4")

        idx, op = arr.GetActivity(frame)
        if op == "get":
            container.patches[idx].set_color("magenta")
        elif op == "set":
            container.patches[idx].set_color("red")

        return(*container, txt)

    ani = FuncAnimation(fig, update, frames=range(
        len(arr.full_copies)), blit=True, interval=2500./FPS, repeat=False)
    return fig, ani


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def delete_figure_agg(figure_agg):
    if figure_agg:
        figure_agg.get_tk_widget().forget()
        plt.close('all')


if __name__ == '__main__':
    run()
