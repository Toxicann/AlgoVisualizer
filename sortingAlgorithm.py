#################################################################
##########################INSERTION SORT#########################
#################################################################

def insertionSort(arr):
    i = 1
    while(i < len(arr)):
        j = i
        while ((j > 0) and (arr[j - 1] > arr[j])):
            # swapping shortcurt in python
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        i += 1

#################################################################
##########################QUICK SORT#############################
#################################################################


def quickSort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quickSort(arr, lo, p - 1)
        quickSort(arr, p + 1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    temp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = temp
    return i

#################################################################
##########################BUBBLE SORT############################
#################################################################


def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#################################################################
##########################SELECTION SORT#########################
#################################################################


def selectionSort(arr, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i

        arr[step], arr[min_idx] = arr[min_idx], arr[step]
