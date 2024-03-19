import copy
from array import array
from typing import Union, List

def selectsort(array: Union[array, List]) -> Union[array, List]:
    """
    Args:
    array: array or list of elements 

    Return:
    An array or list sorted
    """

    sorted_array = copy.deepcopy(array)

    for i in range(len(array)):

        smallest_element = array[i]

        for j in range(i + 1, len(array)):
            if smallest_element > array[j]:
                temp = smallest_element 
                smallest_element = array[j]
                array[j] = temp

        sorted_array[i] = smallest_element

    return sorted_array
