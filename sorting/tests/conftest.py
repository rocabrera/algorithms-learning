import random, copy
from array import array
from typing import List, Tuple, TypeAlias

import pytest

ListTestInterface: TypeAlias = List[Tuple[list, list]]
ArrayTestInterface: TypeAlias = List[Tuple[array, array]]

#############################
# List fixtures
#############################
@pytest.fixture
def list_random_cases() -> ListTestInterface:

    odd =  [1, 2, 3, 4, 5]
    even =  [1, 2, 3, 4, 5, 6]
    double_odd =  [1.0, 2.7, 3.0, 7.0, 10.2]
    double_even =  [1.0, 2.7, 3.0, 7.0, 10.2, 14.9]

    n = 3
    elements = []
    
    for expected in [odd, even, double_odd, double_even]:
        for _ in range(n):
            entry = copy.deepcopy(expected)
            random.shuffle(entry)
            elements.append((entry, expected))
    return elements

@pytest.fixture
def list_edge_cases() -> ListTestInterface:
    odd =  [1, 2, 3, 4, 5]
    even =  [1, 2, 3, 4, 5, 6]

    return [
        ([1,2,3,4,5,6], even),
        ([6,2,3,4,5,1], even),
        ([6,5,4,3,2,1], even),
        ([1,2,3,4,5], odd),
        ([5,2,3,4,1], odd),
        ([5,4,3,2,1], odd)
    ]

@pytest.fixture
def list_duplicated_elements_cases() -> ListTestInterface:
    return [
        ([1,2,3,6,5,6],  [1,2,3,5,6,6]),
        ([6,6,3,4,5,1],  [1,3,4,5,6,6]),
        ([6,3,4,3,2,3],  [2,3,3,3,4,6]),
        ([1,1,3,4,5],  [1,1,3,4,5]),
        ([5,2,3,2,1],  [1,2,2,3,5]),
        ([1,4,3,2,1],  [1,1,2,3,4])
    ]

#############################
# Array fixtures
#############################
@pytest.fixture
def array_random_cases() -> ArrayTestInterface:

    odd =  array('i', [1, 2, 3, 4, 5])
    even =  array('i', [1, 2, 3, 4, 5, 6])
    double_odd =  array('d', [1.0, 2.7, 3.0, 7.0, 10.2])
    double_even =  array('d', [1.0, 2.7, 3.0, 7.0, 10.2, 14.9])

    n = 3
    elements = []
    
    for expected in [odd, even, double_odd, double_even]:
        for _ in range(n):
            entry = copy.deepcopy(expected)
            random.shuffle(entry)
            elements.append((entry, expected))
    return elements

@pytest.fixture
def array_duplicated_elements_cases() -> ArrayTestInterface:
    return [
        (array('i', [1,2,3,6,5,6]), array('i', [1,2,3,5,6,6])),
        (array('i', [6,6,3,4,5,1]), array('i', [1,3,4,5,6,6])),
        (array('i', [6,3,4,3,2,3]), array('i', [2,3,3,3,4,6])),
        (array('i', [1,1,3,4,5]), array('i', [1,1,3,4,5])),
        (array('i', [5,2,3,2,1]), array('i', [1,2,2,3,5])),
        (array('i', [1,4,3,2,1]), array('i', [1,1,2,3,4]))
    ]


@pytest.fixture
def array_edge_cases() -> ArrayTestInterface:
    odd =  array('i', [1, 2, 3, 4, 5])
    even =  array('i', [1, 2, 3, 4, 5, 6])

    return [
        (array('i', [1,2,3,4,5,6]), even),
        (array('i', [6,2,3,4,5,1]), even),
        (array('i', [6,5,4,3,2,1]), even),
        (array('i', [1,2,3,4,5]), odd),
        (array('i', [5,2,3,4,1]), odd),
        (array('i', [5,4,3,2,1]), odd)
    ]

