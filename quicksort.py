'''implemetation of quick sort algorithm from lectures'''

import random

def quick_sort(array):
    ## This may need to go into function parameters
    length = len(array)
    if length == 1:
        return array
    pivot = random.randrange(length)
    semi_sort = partition(array, left, right)


def partition(array, left, right):
    pivot = array[left]
    sort_split = left + 1

    ## not sure if range ends at right or right + 1
    for unsorted in range(length + 1, right + 1):
        if array[break_point] < pivot:
            array[sort_split], array[unsorted] = array[unsorted], \
                                                 array[sort_split]
            sort_split += 1
    array[pivot], array[sort_split -1] = array[sort_split - 1], array[pivot]


# QuickSort(array, length n)
#      if n = 1, return
#      p = choose pivot (A, n) - running time depends on this choice
#      partition A around p
#      recursively sort on both sides of p
# no combine or merge step
#
# Partition (A, l, r)
#      l & r indicate indices of the left-most index (where you're supposed to work) & right-most (boundary between sorted & unsorted??) = l & r bound the sub-array you're working on
#      pi = A[l]
#      i = l + 1
#      for j = l+1 to r:
#           if A[j] > p: do nothing
#           if A[j} < p:
#                Swap A[j] and A[i]
#                     (this will introduce redundant swaps until you find
#                      a result > p)
#                i += 1
#      Swap A[l] and A[i-1]


quick_sort([4,2,3,1])