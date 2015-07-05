'''approaches to solving for number of inversions in an array'''

## setup stuff

import time
problem_array = [line.strip() for line in open("IntegerArray.txt", 'r')]

def brute_force(array):
    '''brute force inversion calculation - quadratic speed'''
    start = time.time()
    inversion_count = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                inversion_count +=1
    print ('Brute force time: ' + str(time.time() - start))
    return inversion_count

def count_inversions(array):
    ''' calculates number of inversions in an array using divide-and conquer approach
    :param array:
    :return: inversion_count:
    '''
    start = time.time()
    inversion_count = sort_and_count(array)[0]
    print ('Count inversions time: ' + str(time.time() - start))
    return inversion_count

def sort_and_count(array):
    '''function to do the main divide-and-conquer work
    returns count of inversions plus a sorted array'''
    inversion_count = 0
    if len(array) <= 1:
        inversion_count += 0
        return_array = array
    elif len(array) == 2:
        if array[0] > array[1]:
            inversion_count += 1
            return_array = [array[1], array[0]]
        else:
            return_array = array
    else:
        left_array = sort_and_count(array[0: int(len(array)/2)])
        right_array = sort_and_count(array[int(len(array)/2):])
        inversion_count += left_array[0]
        inversion_count += right_array[0]
        merge_results = merge_and_count_split_inv(left_array[1], right_array[1])
        inversion_count += merge_results[0]
        return_array = merge_results[1]

    return (inversion_count, return_array)


def merge_and_count_split_inv(array1, array2):
    ''' merges two sorted arrays into one sorted array and counts split inversions
    :param array1, array2:
    :return array:
    '''
    array1_position = 0
    array2_position = 0
    inversion_count = 0
    return_array = []
    while array1_position + array2_position < len(array1) + len(array2):
        if array1[array1_position] < array2[array2_position]:
            return_array.append(array1[array1_position])
            array1_position += 1
            if array1_position == len(array1):
                return_array.extend(array2[array2_position:])
                array2_position = len(array2)
        else:
            return_array.append(array2[array2_position])
            array2_position += 1
            inversion_count += len(array1) - array1_position
            if array2_position == len(array2):
                return_array.extend(array1[array1_position:])
                ## Do I need to augment inversion_count?  I don't think so...
                array1_position = len(array1)

    return (inversion_count, return_array)


def test_inversion():
    '''testing routine'''
    array = [1,2,3,4]
    print ('Array: ' + str(array))
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 0.\n')
    array = [2,1,4,3]
    print ('Array: ' + str(array))
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 2.\n')
    array = [2,1]
    print ('Array: ' + str(array))
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 1.\n')
    array = [1]
    print ('Array: ' + str(array))
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 0.\n')
    array = [2,1,4,3,6,5,8,7,10,9,12,11,14,13,16,15]
    print ('Array: ' + str(array))
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be '
           + str(brute_force(array)) + '.\n')
    array = [4,2,3,1]
    print ('Array: ' + str(array))
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be '
           + str(brute_force(array)) + '.\n')
    array = [4,3,2,1]
    print ('Array: ' + str(array))
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 6.\n')
    array = [8,7,6,5,4,3,2,1]
    print ('Array: ' + str(array))
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 28.\n')
    array = [1,2,3]
    print ('Count Inversions' + str(count_inversions(array)) + '. Answer should be 0')
    array = [1,3,5,2,4,6]
    print ("Brute Force Inversion = " + str(brute_force(array)) + ".  Answer should be 3")
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 3')
    array = [ 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
    print ("Brute Force Inversion = " + str(brute_force(array)) + ".  Answer should be 56")
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 56')
    array = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
    print ("Brute Force Inversion = " + str(brute_force(array)) + ".  Answer should be 590")
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 590')
    array = [76, 85, 59, 142, 67, 51, 133, 64, 42, 128, 9, 153, 169, 114, 193, 162, 90, 77, 14, 154, 151, 182, 18, 160, 197, 26, 143, 178, 137, 166, 1, 74, 152, 122, 185, 10, 78, 107, 84, 113, 116, 28, 175, 124, 129, 89, 30, 29, 163, 49, 40, 101, 66, 19, 80, 119, 135, 57, 38, 104, 73, 32, 146, 2, 91, 99, 190, 58, 132, 23, 194, 75, 167, 79, 123, 112, 199, 131, 60, 55, 47, 174, 17, 168, 52, 155, 109, 200, 161, 136, 195, 111, 25, 71, 145, 88, 24, 81, 186, 16, 130, 179, 68, 65, 83, 156, 53, 148, 4, 196, 33, 50, 3, 94, 34, 45, 36, 147, 35, 70, 62, 69, 191, 141, 22, 46, 183, 126, 87, 13, 159, 103, 127, 144, 8, 11, 41, 189, 198, 54, 56, 108, 176, 106, 173, 97, 21, 164, 98, 172, 171, 170, 149, 110, 138, 31, 125, 63, 82, 192, 39, 92, 95, 15, 7, 105, 187, 180, 5, 6, 44, 102, 134, 188, 181, 139, 184, 177, 12, 115, 61, 165, 37, 140, 100, 157, 20, 150, 43, 117, 120, 48, 27, 121, 86, 96, 158, 72, 118, 93]
    print ('Brute Force Inversion = ' + str(brute_force(array)) + '. Answer should be 9945')
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 9945')
    array = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
    print ('Brute Force Inversion = ' + str(brute_force(array)) + '. Answer should be 0')
    print ('Count Inversions = ' + str(count_inversions(array)) + '. Answer should be 0')



def class_problem():
    # source_file = open('IntegerArray.txt', 'r')
    # array = []
    # number = source_file.readline()
    # while (number != ''):
    #     array.append(int(number))
    #     number = source_file.readline()
    # source_file.close()
    #
    # print ('Calculated answer 1: ' + str(count_inversions(array[:30000])))

    # problem_array = [line.strip() for line in open("IntegerArray.txt", 'r')]
    read_in = [int(line.strip()) for line in open("IntegerArray.txt", 'r')]

    problem_array = read_in[:10000]
    print ('10,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in[:20000]
    print ('20,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in[:30000]
    print ('30,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in[:40000]
    print ('40,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in[:50000]
    print ('50,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in[:60000]
    print ('60,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in[:70000]
    print ('70,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in[:80000]
    print ('80,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in[:90000]
    print ('90,000 Calculated answer: ' + str(count_inversions(problem_array)) + '\n')
    problem_array = read_in
    print ('Full Set Calculated answer: ' + str(count_inversions(problem_array)) + '\n')


# test_inversion()

class_problem()