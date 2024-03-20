from array import array

def quicksort_list(elements: list):
    """
    Sort a list of elements in O(n*logn) time complexity
    """

    if len(elements) < 2:
        return elements 

    pivot = elements[0]

    left = []
    right = []

    for elem in elements[1:]:
        if pivot > elem:
            left.append(elem)
        else:
            right.append(elem)

    return quicksort_list(left) + [pivot] + quicksort_list(right)

# https://www.geeksforgeeks.org/python-program-for-quicksort/
def _quicksort_array(array, low, high):

    if low < high:
        pivot = array[high]
        # Points to the first element greater than the pivot
        i = low 
        for j in range(low, high):
            if array[j] <= pivot:
                # Makes sure elements lower than the pivot are below i 
                (array[i], array[j]) = (array[j], array[i])
                i = i + 1
        # Change the position of the pivot with the first element greater than itself 
        (array[i], array[high]) = (array[high], array[i])
    
        _quicksort_array(array, low, i - 1)
        _quicksort_array(array, i + 1, high)

def quicksort(arr: array):
    low = 0
    high = len(arr) -1
    _quicksort_array(arr, low, high)
    return arr