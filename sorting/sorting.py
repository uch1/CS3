#!python




def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not
    for i in range(len(items)):

        for j in range(i+1, len(items)):
            if items[i] > items[j]:
                return False

    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Swap adjacent items that are out of order

    # Repeat until all items are in sorted order
        for i in range(0, len(item)):
            left_element = items[i]
            right_element = items[i + 1]
            # if left element is greater than right element swap their positions
            if left_element > right_element:
                left_element, right_element = right_element, left_element



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time:
        - Worse Case: it's O(n^2) because we have to iterate over each of the n elements of the array
            and repeat the process n times
        - Best Case: O(n^2) It's not guaranteed that array will be sorted, we have to repeat
            the same process
    TODO: Memory usage: ??? Why and under what conditions?"""

    # if the array is sorted then STOP
    if is_sorted(items):
        return

    # Repeat until all items are in sorted order
    # iterate and get the position of each unsorted element
    for index in range(len(items) - 1):
        # set the first unsorted element as the minimum
        current_minimum = items[index]
        # iterate through the remaining unsorted elements to find the true minimum
        for index2 in range(index + 1, len(items)):
            unsorted_element = items[index2]

            if unsorted_element < current_minimum:
                # unsorted element becomes the new minimum
                #element = minimum
                # current minimum becomes the unsorted element
                current_minimum = unsorted_element
    # swap minimum with first unsorted position
    unsorted_element, current_minimum = current_minimum, unsorted_element

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # items is a given array of unsorted elements
    # TODO: Do this using a for loop
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


    for index in range(1,len(items)):
        current_element = items[index]
        position = index

        while position > 0 and items[position - 1] > current_element:
            items[position] = items[position - 1]
            position = position - 1

        items[position] = current_element
    # Repeat until all items are in sorted order
    # for index in range(1, len(items)):
    #     sorted_element = items[index - 1]
    #     extracted_element = items[index]
    # Mark the first element as sorted
    # i = 0
    # sorted_element = items[i]
    # # Extract the first unsorted element in items:
    # for j in range(len(items)):
    #     # 'j' represents the unsorted elements in items
    #     extracted_element = items[j + 1]
    #     for
    #     if sorted_element > extracted_element:
    #         items[j + 1] = items[i]
    #         # moved sorted element to the right by 1
    #         i += 1
    #     break




def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Repeat until one list is empty
    new_list = []

    # Find minimum item in both lists and append it to new list
    for left_index in range(len(items1) - 1):
        left_item = items1[left_index]

        for right_index in range(len(items2) - 1):
            right_item = items2[right_index]


            if left_item < right_item:
                new_list.append(left_item)
            if right_item < left_item:
                new_list.append(right_item)
            if left_item == right_item:
                new_list.append(left_item)
                new_list.append(right_item)

    # Append remaining items in non-empty list to new list
    if len(new_list) > len(items1) and len(new_list) > len(items2):
        new_list.extend(items1 + items2)

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    mid_point = len(items) // 2
    left_half = items[:mid_point]
    right_half = items[mid_point:]

    # Sort each half using any other sorting algorithm
    selection_sort(left_half)
    selection_sort(right_half)
    # Merge sorted halves into one list in sorted order
    items[:] = merge(items1, items2)

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
