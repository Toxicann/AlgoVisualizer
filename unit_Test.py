import sortingAlgorithm


def insertion(arr):
    sortingAlgorithm.insertionSort(arr)
    return arr


def selection(arr):
    sortingAlgorithm.selectionSort(arr, len(arr))
    return arr


def bubble(arr):
    sortingAlgorithm.bubbleSort(arr)
    return arr


def quick(arr):
    sortingAlgorithm.quickSort(arr, 0, len(arr) - 1)
    return arr


def test_run1():
    assert insertion([2, 6, 3, 7]) == [2, 3, 6, 7]


def test_run2():
    assert selection([1, 7, 3, 9]) == [1, 3, 7, 9]


def test_run3():
    assert bubble([9, 8, 1, 5]) == [1, 5, 8, 9]


def test_run4():
    assert quick([1, 56, 27, 0]) == [0, 1, 27, 56]
