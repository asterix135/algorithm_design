'''implemetation of quick sort algorithm from lectures'''

import random

def sort_array(array):
    quick_sort(array, 0, len(array))

def quick_sort(array, left, right):
    if right - left <= 0:
        return
    pivot = partition(array, left, right)
    quick_sort(array, left, pivot-1)
    quick_sort(array, pivot + 1, right)
    return array


def partition(array, left, right):
    pivot_idx = random.randrange(left, right)
    pivot = array[pivot_idx]
    if pivot_idx != left:
        array[left], array[pivot_idx] = array[pivot_idx], array[left]
    # split_idx refers to the break between higher than pivot & less than pivot
    split_idx = left + 1
    # sort_idx refers to the break between sorted & unsorted elements
    sort_idx = left + 1
    # while sort_idx < right:

    for sort_idx in range(left + 1, right):
        if array[sort_idx] < pivot:
            array[sort_idx], array[split_idx] = \
                array[split_idx], array[sort_idx]
            split_idx += 1
        sort_idx += 1
    array[left], array[split_idx - 1] = array[split_idx - 1], array[left]
    return split_idx -1



def test_routine(array_len):
    input_array = random.sample(range(array_len), array_len)
    sort_array(input_array)
    return input_array


print (test_routine(10))

# print (test_routine(3))
