from tkinter import messagebox
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import StatusBar
import PathfinderVis
import subprocess

from SortingVis import *
from PathfinderLogic import *


sg.theme('dark grey 8')


def sortingWindow():
    sortVal = 4

    button_layout = [
        [sg.Radio('Insertion Sort', disabled=False, font=(20), size=(15, 2), pad=(6, 10), group_id="sort", key='-INS-', enable_events=True),
         sg.Radio('Bubble Sort', font=(20), disabled=False, size=(15, 2), pad=(6, 10), group_id="sort", key='-BBL-', enable_events=True)],
        [sg.Radio('Selection Sort', disabled=False, font=(20), size=(15, 2), pad=(6, 10), group_id="sort", key='-SEL-', enable_events=True),
            sg.Radio('Quick Sort', disabled=False, font=(20), size=(15, 2), pad=(6, 10), group_id="sort", default=True, key='-QCK-', enable_events=True)]
    ]

    slider_layout = [
        [sg.Text("Enter preferred array:")],
        [sg.Input(key='-ARR-', size=(48, 20), enable_events=True)],
        [sg.Text('No. of Bars:')],
        [sg.Slider(orientation='h', range=(2, 100), default_value=15,
                   size=(38, 17), key='-SLIDER-', enable_events=True)],
        [sg.Text('Sorter Speed:')],
        [sg.Slider(orientation='h', range=(1, 4), default_value=3,
                   size=(38, 17), key='-SPEED-', enable_events=True)],
    ]

    leftCol = [
        [sg.Text('Sorting Algorithm', justification='left', font=('Arial', 32))],
        [sg.Text('Instructions', justification='left', font=(
            'Arial', 22), key='-SORTNAME-')],
        [sg.Text('Choose the algorithms you want, its size and speed on the right side of the window. Generate a random array or input your own array for sorting visualization.', size=(32, 10), justification='left', font=(
            'Arial', 14), key='-SORTDESC-')],
        [sg.Text('UI Representation', justification='left', font=(
            'Arial', 18), key='-TIMECOMPLEX-')],
        [sg.Text('Accesses refers to the times array has been accessed', size=(30, 2), justification='left', font=(
            'Arial', 14), key='-BESTCASE-')],
        [sg.Text('Green color represents accesses', size=(30, 2), justification='left', font=(
            'Arial', 14), key='-AVERAGECASE-')],
        [sg.Text('Red color represents changes', size=(30, 2), justification='left', font=(
            'Arial', 14), key='-WORSTCASE-')],

    ]

    midCol = [
        [sg.Canvas(background_color='white', size=(720, 715), key='-CANVAS-')]
    ]

    rightCol = [
        [sg.Text('Sorting Visualizer', justification='center', font=('Arial', 32))],
        [sg.Text('Choose Your Desired Algortihm',
                 justification='center', font=('Arial', 16))],
        [sg.Text('', size=(10, 2))],
        [sg.Frame('Sorting Algorithms', button_layout)],
        [sg.Text('', size=(10, 2))],
        [sg.Frame('Advanced Settings', slider_layout)],
        [sg.Text('', size=(10, 1))],
        [sg.Button('Generate', font=(20), size=(15, 2), pad=(10, 10), key='-GEN-'),
            sg.Button('Clear', font=(20), size=(15, 2), pad=(10, 10), key='-CLR-')]

    ]

    layout = [
        [
            sg.Column(leftCol, justification='left'),
            sg.VSeparator(),
            sg.Column(midCol),
            sg.VSeparator(),
            sg.Column(rightCol, vertical_alignment='center',
                      element_justification='center')
        ]
    ]

    window = sg.Window('Sorting Visualizer', layout, size=(1540, 750))

    figure_agg = None
    while True:
        eventSort, valueSort = window.read()

        if eventSort == sg.WIN_CLOSED:
            break

        if eventSort == '-INS-':
            sortVal = 1
            window['-SORTNAME-'].update("Insertion Sort")
            window['-SORTDESC-'].update("Insertion sort works similar to the sorting of playing cards in hands. It is assumed that the first card is already sorted in the card game, and then we select an unsorted card. If the selected unsorted card is greater than the first card, it will be placed at the right side; otherwise, it will be placed at the left side. Similarly, all unsorted cards are taken and put in their exact place.")
            window['-TIMECOMPLEX-'].update("Time Complexity:")
            window['-BESTCASE-'].update("Best Case: O(n)")
            window['-AVERAGECASE-'].update("Average Case: O(n^2)")
            window['-WORSTCASE-'].update("Worst Case: O(n^2)")
        elif eventSort == '-BBL-':
            sortVal = 2
            window['-SORTNAME-'].update("Bubble Sort")
            window['-SORTDESC-'].update(
                "Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.")
            window['-TIMECOMPLEX-'].update("Time Complexity:")
            window['-BESTCASE-'].update("Best Case: O(n)")
            window['-AVERAGECASE-'].update("Average Case: O(n^2)")
            window['-WORSTCASE-'].update("Worst Case: O(n^2)")
        elif eventSort == '-SEL-':
            sortVal = 3
            window['-SORTNAME-'].update("Selection Sort")
            window['-SORTDESC-'].update(
                "Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.")
            window['-TIMECOMPLEX-'].update("Time Complexity:")
            window['-BESTCASE-'].update("Best Case: O(n^2)")
            window['-AVERAGECASE-'].update("Average Case: O(n^2)")
            window['-WORSTCASE-'].update("Worst Case: O(n^2)")
        elif eventSort == '-QCK-':
            sortVal = 4
            window['-SORTNAME-'].update("Quick Sort")
            window['-SORTDESC-'].update(
                "QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.")
            window['-TIMECOMPLEX-'].update("Time Complexity:")
            window['-BESTCASE-'].update("Best Case: O(nLogn)")
            window['-AVERAGECASE-'].update("Average Case: O(nLogn)")
            window['-WORSTCASE-'].update("Worst Case: O(n^2)")

        if eventSort == '-GEN-':
            delete_figure_agg(figure_agg)
            window['-CANVAS-'].update()
            myVals.getVal(valueSort['-SLIDER-'], sortVal,
                          valueSort['-SPEED-'], valueSort['-ARR-'])
            fig, ani = run()
            figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

        if eventSort == '-CLR-':
            delete_figure_agg(figure_agg)

    window.close()


def mainWindow():
    leftCol = [[sg.Image('logo.png', key='-IMG-', size=(500, 725))]]

    rightCol = [
        [sg.Text("AlgoVisualizer", justification='center',
                 font=('Arial', 32), size=(60, 1))],
        [sg.Text("A way to make learning Algorithms Simpler",
                 justification='center', font=('Arial', 21), size=(60, 1))],
        [sg.Text("Choose Your Preferred Algorithm Sub-Group",
                 justification='center', font=('Arial', 16), size=(60, 1))],
        [sg.Text("_" * 150)],
        [sg.Text(" ", size=(50, 5))],
        [sg.Button("Sorting Algorithm", font=('Arial', 20),
                   pad=(4, 2), size=(20, 2), key='-SORTWIN-')],
        [sg.Text(" ", size=(50, 1))],
        [sg.Button("PathFinding Algorithm", disabled=False, font=(
            'Arial', 20), pad=(4, 2), size=(20, 2), key='-PATHWIN-')]
    ]

    layout = [
        [
            sg.Column(leftCol),
            sg.VSeparator(),
            sg.Column(rightCol, vertical_alignment='center',
                      element_justification='center')
        ]
    ]

    window = sg.Window("AlgoVisualizer", layout, size=(1200, 750))

    while True:
        eventMain, valueMain = window.read()

        if eventMain == sg.WIN_CLOSED:
            break

        if eventMain == '-SORTWIN-':
            window.hide()
            sortingWindow()
            window.un_hide()

        elif eventMain == '-PATHWIN-':
            window.hide()
            subprocess.run(['python', 'PathfinderVis.py'])
            window.un_hide()

    window.close()


if __name__ == '__main__':
    mainWindow()
