"""Implements pseudo-random number generation."""
import rand


def merge_sort(arr):
    """ Perform merge sort on an array.

    Argument:
    arr -- array to sort

    Returns:
    A sorted array containing the elements of the input array in ascending order
    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """ Helping function for merge sort to merge two sorted arrays for result.

    Arguments:
    left_arr -- sorted array representing left half of split
    right_arr -- sorted array representing right half of split

    Returns:
    A single sorted array
    """
    left_index = 0
    right_index = 0
    insert_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[insert_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[insert_index] = right_arr[right_index]
            right_index += 1
        insert_index += 1
    for i in range(left_index, len(left_arr)):
        merge_arr[insert_index] = left_arr[i]
        insert_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[insert_index] = right_arr[i]
        insert_index += 1

    return merge_arr


array = rand.random_array([None] * 20)
arr_out = merge_sort(array)

print(arr_out)
