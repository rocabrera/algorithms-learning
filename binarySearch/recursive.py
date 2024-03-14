import math
import array as arr

def binary_search(array: arr, left:int, right:int, k: int):
    """
    Args:
    
    array: a ordered array
    k: element to search for
    left: first index of array
    right: last index of array

    Return:
    If element is found return its index otherwise -1

    """

    middle = math.ceil((left + right) / 2)
    
    if left > right:
        return -1

    if k == array[middle]:
        return middle

    if k > array[middle]:
        left = middle + 1
    else:
        right = middle - 1

    return binary_search(array, left, right, k)
