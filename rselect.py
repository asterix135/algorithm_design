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
        array_copy = list(array)
        pivot = partition(array_copy)
        if pivot == istat:
            return array_copy[pivot]
        elif pivot > istat:
            return rselect(array_copy[:pivot], istat)
        else:
            return rselect(array_copy[pivot+1:], istat-pivot-1)


def partition(array):
    """
    partition array to find ith statistic
    """
    # random.seed(0)
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


def test():
    """Testing routine"""
    array = [1,5,3,2,4,6,0,7,8]
    i_element = 4
    # array = [2,0,1]
    print(rselect(array, i_element))
    import quicksort
    quicksort.sort_array(array)
    print(array[i_element])

def random_test(array_len):
    """Test on randomized array"""
    input_array = random.sample(range(array_len), array_len)
    i_element = array_len // 2
    print("algorithm result")
    print(rselect(input_array, i_element))
    import quicksort
    quicksort.sort_array(input_array)
    print('quicksort results')
    print(input_array[i_element])

def random_test_battery():
    for i in range(5,5006,1000):
        print("array length: " + str(i))
        random_test(i)
        print()

# random_test_battery()