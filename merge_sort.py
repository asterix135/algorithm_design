'''Functions to implement Merge/sort algorithm'''


def merge_sort(lst, idx = 0):
    '''Main merge/sort function to call
    takes a list as input and sorts in numerical order
    can take an optional idx parameter, if the elements of the list are iterable - will sort on index position'''
    if len(lst) == 2:
        if lst[0][idx] > lst[1][idx]:
            return [lst[1], lst[0]]
        else:
            return lst
    elif len(lst) <= 1:
        return lst
    else:
        list_a = merge_sort(lst[:len(lst)//2], idx)
        list_b = merge_sort(lst[len(lst)//2:], idx)
        output_list = merge(list_a, list_b, idx)
        return output_list

def merge(list_a, list_b, idx):
    '''merge subroutine called from merge_sort
    takes two sorted sub-lists and merges them into one'''
    output_list = []
    list_a_position = 0
    list_b_position = 0
    while list_a_position + list_b_position < len(list_a) + len(list_b):
        if list_a[list_a_position][idx] < list_b[list_b_position][idx]:
            output_list.append(list_a[list_a_position])
            list_a_position += 1
            if list_a_position == len(list_a):
                output_list.extend(list_b[list_b_position:])
                list_b_position = len(list_b)
        else:
            output_list.append(list_b[list_b_position])
            list_b_position += 1
            if list_b_position == len(list_b):
                output_list.extend(list_a[list_a_position:])
                list_a_position = len(list_a)
    return output_list


