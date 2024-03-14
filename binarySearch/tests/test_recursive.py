import array as arr
import pytest
from recursive import binary_search 

odd_integer_array = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
even_integer_array = arr.array('i', [1, 2, 3, 4, 5, 6])
odd_double_array = arr.array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
even_double_array = arr.array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

@pytest.mark.parametrize("array,k,expected_index", [
    (odd_integer_array, 5, 4),
    (odd_integer_array, 2, 1),
    (even_integer_array, 3, 2),
    (even_integer_array, 4, 3),
    (odd_double_array, 5.0, 4),
    (odd_double_array, 2.0, 1),
    (even_double_array, 3.0, 2),
    (even_double_array, 4.0, 3)
])
def test_base_case(array, k, expected_index):
    left = 0
    right = len(array) - 1
    result = binary_search(array=array, left=left, right=right, k=k)
    assert result == expected_index

@pytest.mark.parametrize("array,k,expected_index", [
    (odd_integer_array, 1, 0),
    (odd_integer_array, 7, 6), 
    (even_integer_array, 1, 0),
    (even_integer_array, 6, 5), 
    (odd_double_array, 1.0, 0),
    (odd_double_array, 7.0, 6), 
    (even_double_array, 1.0, 0),
    (even_double_array, 6.0, 5)
])
def test_limits(array, k, expected_index):
    left = 0
    right = len(array) - 1
    result = binary_search(array=array, left=left, right=right, k=k)
    assert result == expected_index
