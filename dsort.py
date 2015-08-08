"""
Deterministic selection algorithm

Pseudocode:
Dselect(array A, length n, order statistics i)
ChoosePivot subroutine
1) break A into groups of 5, sort each group (eg using merge/sort)
2) C = the n/5 'middle elements'
3) p = Select(C, n/5, n/10) (recursively computes median of C)
Back to main routine
4) partition A around p
5) if j=i, return p
6) if j<i, return Select(1st part of A, j-1, i)
7) if j>i, return Select(2nd part of A, n-j, i-j)
"""

import merge_sort
import math

def dselect(array, istat):
    if len(array) <= 5:  # should this be 10?
        sorted_array = merge_sort.merge_sort(array)
        return sorted_array[istat]
    else:
        groups_of_5 = []
        for group_start in range(0, len(array) - 4, 5):
            group = array[group_start:group_start + 5]
            group_median_pos = math.ceil(len(group) / 2) - len(group) % 2
            groups_of_5.append(dselect(group, int(group_median_pos)))
        median_of_medians = dselect(groups_of_5, len(array)//10)
        below = []
        above = []
        pivot = []
        for num in range(len(array)):
            if array[num] == median_of_medians:
                pivot.append(array[num])
            elif array[num] < median_of_medians:
                below.append(array[num])
            else:
                above.append(array[num])
        if istat < len(below):
            return dselect(below, istat)
        elif istat >= len(below) + len (pivot):
            return dselect(above, istat - len(below) - len(pivot))
        else:
            return median_of_medians

