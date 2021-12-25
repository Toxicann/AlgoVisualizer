from tkinter import messagebox
import PySimpleGUI as sg

from SortingVis import *

sg.theme('dark grey 8')


def sortingWindow():
    sortVal = 4

    button_layout = [
        [sg.Radio('Insertion Sort', disabled=False, font=(20), size=(15, 2), pad=(6, 10), group_id="sort", key='-INS-', enable_events=True),
         sg.Radio('Bubble Sort', font=(20), disabled=False, size=(15, 2), pad=(6, 10), group_id="sort", key='-BBL-', enable_events=True)],
        [sg.Radio('Selection Sort', disabled=False, font=(20), size=(15, 2), pad=(6, 10), group_id="sort", key='-SEL-', enable_events=True),
            sg.Radio('Quick Sort', disabled=False, font=(20), size=(15, 2), pad=(6, 10), group_id="sort", default=True, key='-QCK-', enable_events=True)]
    ]

    leftCol = [
        [sg.Canvas(background_color='white', size=(720, 715), key='-CANVAS-')]
    ]

    rightCol = [
        [sg.Text('Sorting Visualizer', justification='center', font=('Arial', 32))],
        [sg.Text('Choose Your Desired Algortihm',
                 justification='center', font=('Arial', 16))],
        [sg.Text('', size=(10, 2))],
        [sg.Frame('Sorting Algorithms', button_layout)],
        [sg.Text('', size=(10, 2))],
        [sg.Slider(orientation='h', range=(2, 100), default_value=45,
                   size=(40, 20), key='-SLIDER-', enable_events=True)],
        [sg.Text('', size=(10, 1))],
        [sg.Button('Generate', font=(20), size=(15, 2), pad=(10, 10), key='-GEN-'),
            sg.Button('Clear', font=(20), size=(15, 2), pad=(10, 10), key='-CLR-')]

    ]

    layout = [
        [
            sg.Column(leftCol),
            sg.VSeparator(),
            sg.Column(rightCol, vertical_alignment='center',
                      element_justification='center')
        ]
    ]

    window = sg.Window('Sorting Visualizer', layout, size=(1200, 750))

    figure_agg = None
    while True:
        eventSort, valueSort = window.read()

        if eventSort == sg.WIN_CLOSED:
            break

        if eventSort == '-INS-':
            sortVal = 1
        elif eventSort == '-BBL-':
            sortVal = 2
        elif eventSort == '-SEL-':
            sortVal = 3
        elif eventSort == '-QCK-':
            sortVal = 4

        if eventSort == '-GEN-':
            window['-CANVAS-'].update('')
            myVals.getVal(valueSort['-SLIDER-'], sortVal)
            fig, ani = run()
            figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

        if eventSort == '-CLR-':
            delete_figure_agg(figure_agg)

    window.close()


def mainWindow():
    leftCol = [[sg.Image('logo.gif', key='-IMG-', size=(500, 725))]]

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
            messagebox.showinfo(title="Pathfinding",
                                message="Please contact Developer (WIP)")
            window.un_hide()

    window.close()

if __name__ == '__main__':
    mainWindow()
