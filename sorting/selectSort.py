import copy
import array as arr

def selectsort(array: arr) -> arr:
    """
    Args:
    array: array of elements 

    Return:
    An array sorted
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
