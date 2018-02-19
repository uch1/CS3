left_side#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index < len(array):
        if item == array[index]:
            return index

    return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left_side = 0
    right_side = len(array) - 1

    if item == array[left_side]:
        return left_side

    if item == array[right_side]:
        return right_side

    while left_side <= right_side:

        # start at the midpoint of the array
        midpoint = (left_side + right_side) / 2

        if item == array[midpoint]:
            return midpoint

        if item > array[midpoint]:
            right_side = midpoint + 1

        if item < array[midpoint]:
            left_side = midpoint - 1



def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if left <= right:
        midpoint = (left + right) / 2

        if item == array[midpoint]:
            return midpoint

        elif item < array[midpoint]:
            right = midpoint - 1
            return binary_search_recursive(array, item, left, right)

        elif item > array[midpoint]:
            left = midpoint + 1
            return binary_search_recursive(array, item, left, right)
