import math
import array as arr

def binary_search(array: arr, k: int):
    """
    Args:
    
    array: a ordered array
    k: element to search for

    Returns:
    If element is found return its index otherwise -1
    """

    left = 0
    right = len(array) - 1

    while left <= right:
        middle = math.ceil((left + right) / 2)
        if k == array[middle]:
            return middle 
        if k > array[middle]:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1
