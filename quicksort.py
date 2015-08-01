'''implemetation of quick sort algorithm from lectures'''

import random

def sort_array(array):
    '''base call to sort algorithm'''
    quick_sort(array, 0, len(array)-1)

def quick_sort(array, left, right):
    '''primary recursive subroutine'''
    if right - left <= 0:
        return
    pivot = partition(array, left, right)
    quick_sort(array, left, pivot - 1)
    quick_sort(array, pivot + 1, right)


def partition(array, left, right):
    '''sub-routine that actually does the sorting'''
    pivot_idx = random.randrange(left, right)
    pivot = array[pivot_idx]
    if pivot_idx != left:
        array[left], array[pivot_idx] = array[pivot_idx], array[left]
    # split_idx refers to the break between higher than pivot & less than pivot
    split_idx = left + 1
    # sort_idx refers to the break between sorted & unsorted elements
    for sort_idx in range(left + 1, right + 1):
        if array[sort_idx] < pivot:
            array[sort_idx], array[split_idx] = \
                array[split_idx], array[sort_idx]
            split_idx += 1
        sort_idx += 1
    array[left], array[split_idx - 1] = array[split_idx - 1], array[left]
    return split_idx -1

def test_routine(array_len):
    '''testing array on randomized array'''
    input_array = random.sample(range(array_len), array_len)
    sort_array(input_array)
    return input_array


# print (test_routine(22))
