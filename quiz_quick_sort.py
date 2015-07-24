'''implemetation of quick sort algorithm for programming questions'''

m_count = 0

def sort_array(array, sub_option=3):
    """
    Main call - sub_option refers to problem number in homeowork
    array is actually a list
    """
    quick_sort(array, 0, len(array)-1, sub_option)

def quick_sort(array, left, right, sub_option):
    """
    primary recursive algorithm
    """
    global m_count
    if right >= left:
        m_count +=  right - left
    if right - left <= 0:
        return
    pivot = partition(array, left, right, sub_option)
    quick_sort(array, left, pivot - 1, sub_option)
    quick_sort(array, pivot + 1, right, sub_option)


def partition(array, left, right, sub_option):
    """
    Sort elements before and after pivot.  Pivot point is determined by
    sub-option: 1 = fist element in list,  2 = last item in list
    3 = median of first, last & median element in list
    """
    if sub_option == 2:
        array[left], array[right] = array[right], array[left]
    elif sub_option == 3:
        left_val = array[left]
        right_val = array[right]
        mid_idx = ((right - left) // 2) + left
        mid_val = array[mid_idx]
        if left_val < mid_val < right_val or right_val < mid_val < left_val:
            array[left], array[mid_idx] = array[mid_idx], array[left]
        elif left_val < right_val < mid_val or mid_val < right_val < left_val:
            array[left], array[right] = array[right], array[left]
    pivot = array[left]
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



def test_routine():
    """Verification tests"""
    global m_count
    data1 = [int(line.strip()) for line in open('test_10.txt', 'r')]
    m_count = 0
    sort_array(data1, 1)
    print (str(m_count) + ' should be 25')
    data1 = [int(line.strip()) for line in open('test_10.txt', 'r')]
    m_count = 0
    sort_array(data1, 2)
    print (str(m_count) + ' should be 29')
    data1 = [int(line.strip()) for line in open('test_10.txt', 'r')]
    m_count = 0
    sort_array(data1, 3)
    print (str(m_count) + ' should be 21')
    print()


    data2 = [int(line.strip()) for line in open('test_100.txt', 'r')]
    m_count = 0
    sort_array(data2, 1)
    print (str(m_count) + ' should be 615')
    data2 = [int(line.strip()) for line in open('test_100.txt', 'r')]
    m_count = 0
    sort_array(data2, 2)
    print (str(m_count) + ' should be 587')
    data2 = [int(line.strip()) for line in open('test_100.txt', 'r')]
    m_count = 0
    sort_array(data2, 3)
    print (str(m_count) + ' should be 518')
    print()


    data3 = [int(line.strip()) for line in open('test_1000.txt', 'r')]
    m_count = 0
    sort_array(data3, 1)
    print (str(m_count) + ' should be 10297')
    data3 = [int(line.strip()) for line in open('test_1000.txt', 'r')]
    m_count = 0
    sort_array(data3, 2)
    print (str(m_count) + ' should be 10184')
    data3 = [int(line.strip()) for line in open('test_1000.txt', 'r')]
    m_count = 0
    sort_array(data3, 3)
    print (str(m_count) + ' should be 8921')


def homework_problem():
    """
    Runs quicksort & returns number of comparisons on homework list
    """
    global m_count
    quiz_file = [int(line.strip()) for line in open("QuickSort.txt", 'r')]
    m_count = 0
    sort_array(quiz_file, 1)
    print('Question One Answer: ' + str(m_count) + '\n')

    quiz_file = [int(line.strip()) for line in open("QuickSort.txt", 'r')]
    m_count = 0
    sort_array(quiz_file, 2)
    print('Question Two Answer: ' + str(m_count) + '\n')

    quiz_file = [int(line.strip()) for line in open("QuickSort.txt", 'r')]
    m_count = 0
    sort_array(quiz_file, 3)
    print('Question Three Answer: ' + str(m_count) + '\n')

# test_routine()

homework_problem()
