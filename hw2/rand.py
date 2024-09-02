"""Imports subprocess to run the shuf command."""
import subprocess

def random_array(arr):
    """ Randomizes an array.

    Argument:
    arr -- array to randomize

    Returns:
    A randomized version of the given array
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
