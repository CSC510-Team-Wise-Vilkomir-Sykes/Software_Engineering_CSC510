
from hw2_debugging import merge_sort 

# Test Case 1: Unsorted array
def test_unsorted():
    arr = [5, 3, 2, 1, 8, 4, 10, 11, 9, 6, 111, 7]
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 111]
    assert merge_sort(arr) == sorted_arr

# Test Case 2: Sorted array
def test_sorted():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 111]
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 111]
    assert merge_sort(arr) == sorted_arr

# Test Case 3: Empty array
def test_empty():
    arr = []
    sorted_arr = []
    assert merge_sort(arr) == sorted_arr

# # Test Case 4: Duplicated values
# def test_duplicated():
#     arr = [5, 3, 2, 1, 7, 3, 9, 11, 9, 5, 11, 7, 1]
#     sorted_arr = [1, 1, 2, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11]
#     assert merge_sort(arr) == sorted_arr
