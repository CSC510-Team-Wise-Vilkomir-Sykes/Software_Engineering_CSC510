"""Module provides test cases for group project"""
from hw2_debugging import merge_sort

def test_unsorted():
    """Test Case 1: Unsorted array"""
    arr = [5, 3, 2, 1, 8, 4, 10, 11, 9, 6, 111, 7]
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 111]
    assert merge_sort(arr) == sorted_arr

def test_sorted():
    """Test Case 2: Sorted array"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 111]
    sorted_arr = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 111]
    assert merge_sort(arr) == sorted_arr

def test_empty():
    """Test Case 3: Empty array"""
    arr = []
    sorted_arr = []
    assert merge_sort(arr) == sorted_arr
