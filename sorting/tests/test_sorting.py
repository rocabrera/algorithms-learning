import pytest
from quickSort import quicksort_list
from selectSort import selectsort


#############################
# List tests
#############################
@pytest.mark.parametrize("sorting_algorithm",
    [(selectsort), (quicksort_list)],
)
def test_random_for_list(list_random_cases, sorting_algorithm):
    
    for case in list_random_cases:
        entry , expected = case
        result = sorting_algorithm(entry)
        assert result == expected

@pytest.mark.parametrize("sorting_algorithm",
    [(selectsort), (quicksort_list)],
)
def test_edge_for_list(list_edge_cases, sorting_algorithm):

    for case in list_edge_cases:
        entry , expected = case
        result = sorting_algorithm(entry)
        assert result == expected

@pytest.mark.parametrize("sorting_algorithm",
    [(selectsort), (quicksort_list)],
)
def test_duplicated_for_list(list_edge_cases, sorting_algorithm):

    for case in list_edge_cases:
        entry , expected = case
        result = sorting_algorithm(entry)
        assert result == expected

#############################
# Array tests
#############################
@pytest.mark.parametrize("sorting_algorithm",
    [(selectsort)],
)
def test_random_for_array(array_random_cases, sorting_algorithm):
    
    for case in array_random_cases:
        entry , expected = case
        result = sorting_algorithm(entry)
        assert result == expected

@pytest.mark.parametrize("sorting_algorithm",
    [(selectsort)],
)
def test_edge_for_array(array_edge_cases, sorting_algorithm):

    for case in array_edge_cases:
        entry , expected = case
        result = sorting_algorithm(entry)
        assert result == expected

@pytest.mark.parametrize("sorting_algorithm",
    [(selectsort)],
)
def test_duplicated_for_array(array_duplicated_elements_cases, sorting_algorithm):

    for case in array_duplicated_elements_cases:
        entry , expected = case
        result = sorting_algorithm(entry)
        assert result == expected