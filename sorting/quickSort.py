# import copy
# import array as arr

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


