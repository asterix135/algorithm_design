'''implemetation of quick sort algorithm for programming questions'''

# import random
import urllib.request

m_count = 0

def sort_array(array, sub_option):
    ## note - you have to make the starting right len(array) - 1 for the
    ## for loop to work correctly in partition
    quick_sort(array, 0, len(array)-1, sub_option)

def quick_sort(array, left, right, sub_option):
    global m_count
    m_count +=  (right - left)
    if right - left <= 0:
        return
    pivot = partition(array, left, right, sub_option)
    quick_sort(array, left, pivot - 1, sub_option)
    quick_sort(array, pivot + 1, right, sub_option)


def partition(array, left, right, sub_option):
    if sub_option == 2:
        array[left], array[right] = array[right], array[left]
    elif sub_option == 3:
        left_val = array[left]
        right_val = array[right]
        mid_idx = (right - left) // 2
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
    global m_count
    url1 = 'https://dl.dropboxusercontent.com/u/20888180/AlgI_wk2_testcases/10.txt'
    file1 = urllib.request.urlopen(url1)
    data1 = [int(line.strip()) for line in file1]
    m_count = 0
    sort_array(data1, 1)
    print (data1)
    print (str(m_count) + ' should be 25')
    file1 = urllib.request.urlopen(url1)
    data1 = [int(line.strip()) for line in file1]
    print (data1)
    m_count = 0
    sort_array(data1, 2)
    print (data1)
    print (str(m_count) + ' should be 29')
    file1 = urllib.request.urlopen(url1)
    data1 = [int(line.strip()) for line in file1]
    print (data1)
    m_count = 0
    sort_array(data1, 3)
    print (data1)
    print (str(m_count) + ' should be 21')


    # url2 = 'https://dl.dropboxusercontent.com/u/20888180/AlgI_wk2_testcases/100.txt'
    # file2 = urllib.request.urlopen(url2)
    # data2 = [int(line.strip()) for line in file2]
    # m_count = 0
    # sort_array(data2, 1)
    # print (str(m_count) + ' should be 615')
    # file2 = urllib.request.urlopen(url2)
    # data2 = [int(line.strip()) for line in file2]
    # m_count = 0
    # sort_array(data2, 2)
    # print (str(m_count) + ' should be 587')
    # file2 = urllib.request.urlopen(url2)
    # data2 = [int(line.strip()) for line in file2]
    # m_count = 0
    # sort_array(data2, 3)
    # print (str(m_count) + ' should be 518')
    #
    #
    # url3 = 'https://dl.dropboxusercontent.com/u/20888180/AlgI_wk2_testcases/1000.txt'
    # file3 = urllib.request.urlopen(url3)
    # data3 = [int(line.strip()) for line in file3]
    # m_count = 0
    # sort_array(data3, 1)
    # print (str(m_count) + ' should be 10297')
    # file3 = urllib.request.urlopen(url3)
    # data3 = [int(line.strip()) for line in file3]
    # m_count = 0
    # sort_array(data3, 2)
    # print (str(m_count) + ' should be 10184')
    # file3 = urllib.request.urlopen(url3)
    # data3 = [int(line.strip()) for line in file3]
    # m_count = 0
    # sort_array(data3, 3)
    # print (str(m_count) + ' should be 8921')





print (test_routine())

# quiz_file = [int(line.strip()) for line in open("QuickSort.txt", 'r')]

