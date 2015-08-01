import random

def rselect(array, istat):
    """
    Algorithm to return ith order element of an array
    takes array (list) as input
    ith order counted in normal, not pythonic way
    Will not modify original array

    Pseudocode:
    RSelect(array A, length n, order statistic i)
     if n=1, return A[1]
     else
          choose pivot p uniformly at random
          partition A around p
          let j = position of pivot in array (pivot is jth order statistic)
          if i == j
               return p
          if j > i
               return RSelect (1st part of A, j-1, i)
          if j < i
               return RSelect (2nd part of A, n-j, i-j)
    """
    if len(array) == 1:
        return array[0]
    else:
        pivot = partition(array)
        if pivot == istat:
            return array[pivot]
        elif pivot > istat:
            return rselect(array[:pivot-1], istat)
        else:
            return rselect(array[pivot+1:], istat-pivot)


def partition(array):
    """
    partition array to find ith statistic
    """
    pivot_idx = random.randrange(len(array))
    pivot = array[pivot_idx]
    if pivot_idx != 0:
        array[0], array[pivot_idx] = array[pivot_idx], array[0]
    # split_idx refers to the break between higher than pivot & less than pivot
    split_idx = 1
    # sort_idx refers to the break between sorted & unsorted elements
    for sort_idx in range(1, len(array)):
        if array[sort_idx] < pivot:
            array[sort_idx], array[split_idx] = \
                array[split_idx], array[sort_idx]
            split_idx += 1
        sort_idx += 1
    array[0], array[split_idx - 1] = array[split_idx - 1], array[0]
    return split_idx -1





# import quicksort #maybe to re-use partition
#
#
# def select_ith_order(array, istat):
#     """
#     main routine to find ith order statistic of an array
#     takes array (list) as input
#     returns ith order statistic
#     ith order counted in normal, not pythonic way
#     Will not modify original array
#     """
#     array_copy = list(array)
#     return rselect(array_copy, 0, len(array_copy) -1, istat -1)
#
#
#
# def rselect(array, left, right, istat):
#     """
#     Algorithm to return ith order element of an array
#
#     Pseudocode:
#     RSelect(array A, length n, order statistic i)
#      if n=1, return A[1]
#      else
#           choose pivot p uniformly at random
#           partition A around p
#           let j = position of pivot in array (pivot is jth order statistic)
#           if i == j
#                return p
#           if j > i
#                return RSelect (1st part of A, j-1, i)
#           if j < i
#                return RSelect (2nd part of A, n-j, i-j)
#     """
#     if right-left <= 0:
#         return array[left:right+1][0]
#     else:
#         pivot = quicksort.partition(array, left, right)
#         if pivot == istat:
#             return pivot
#         elif pivot > istat:
#             a = rselect(array, left, pivot-1, istat)
#             print(a)
#             return a
#             # return rselect(array, left, pivot-1, istat)
#         else:
#             a = rselect(array, pivot + 1, right, istat - pivot)
#             print(a)
#             return a
#             # return rselect(array, pivot + 1, right, istat - pivot)
#
#
#
#
def test():
    """Testing routine"""
    array = [1,5,3,2,4,6,0,7]
    # array = [2,4,0,3,1]
    print(rselect(array, 5))
    print(array)

test()
