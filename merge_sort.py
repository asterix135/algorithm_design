'''Functions to implement Merge/sort algorithm'''

import random
LIST_LENGTH = 10000
RANDOM_LIST = random.sample(range(LIST_LENGTH), LIST_LENGTH)
# RANDOM_LIST = [4,3,2,1]

def split_sort(number_list):
    '''Takes a list and sorts it in ascending order'''
    if len(number_list) == 2:
        if number_list[0] > number_list[1]:
            return [number_list[1], number_list[0]]
        else:
            return [number_list[0], number_list[1]]
    elif len(number_list) == 1:
        return number_list
    else:
        output_list = []
        list_a = split_sort(number_list[0:int(len(number_list)/2)])
        list_b = split_sort(number_list[int(len(number_list)/2):])
        list_a_position = 0
        list_b_position = 0
        while list_a_position + list_b_position <len(number_list):
            if list_a[list_a_position] < list_b[list_b_position]:
                output_list.append(list_a[list_a_position])
                list_a_position += 1
                if list_a_position == len(list_a):
                    output_list.extend(list_b[list_b_position:])
                    list_a_position = len(number_list)
            else:
                output_list.append(list_b[list_b_position])
                list_b_position += 1
                if list_b_position == len(list_b):
                    output_list.extend(list_a[list_a_position:])
                    list_b_position = len(number_list)

        return output_list



test_result = split_sort(RANDOM_LIST)
print (test_result[0], test_result[len(test_result) -1], test_result[int(len(test_result)/2)])