'''routine to calculate closest set of pairs in a 2-d plane'''

## setup stuff
import time
import math
import merge_sort as ms

def euc_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def brute_force(lst):
    start = time.time()
    closest_distance = float('inf')
    closest_pair = [(),()]
    for point1 in range(len(lst)-1):
        for point2 in range(point1 + 1,len(lst)):
            if euc_distance(lst[point1], lst[point2]) < closest_distance:
                closest_distance = euc_distance(lst[point1], lst[point2])
                closest_pair[0] = lst[point1]
                closest_pair[1] = lst[point2]
    print ('brute force elapsed time: ' + str(time.time() - start))
    return [closest_distance, closest_pair]


def closest_pair(lst):
    start = time.time()
    x_sort = ms.merge_sort(lst, 0)
    y_sort = ms.merge_sort(lst, 1)
    solution = cp_split(x_sort, y_sort)
    print ("closest pair run time: " + str(time.time() - start))
    return solution

def cp_split(x_list, y_list):
    if len(x_list) <= 3:
        return brute_force(x_list)
    else:
        x_left = x_list[:len(x_list)//2]
        x_right = x_list[len(x_list)//2:]
        x_bar = x_left[-1]
        y_left = [val for val in y_list if val[0] <= x_bar[0]]
        y_right = [val for val in y_list if val[0] > x_bar[0]]
        left_best = cp_split(x_left, y_left)
        right_best = cp_split(x_right, y_right)
        if left_best[0] < right_best[0]:
            delta = left_best[0]
            best_pair = left_best[1]
        else:
            delta = right_best[0]
            best_pair = right_best[1]
        split_best = closest_split_pair(x_list, y_list, delta, best_pair)
        if delta > split_best[0]:
            delta = split_best[0]
            best_pair = split_best[1]
        return [delta, best_pair]


def closest_split_pair(x_list, y_list, delta, best_pair):

    ## closest split pair takes 3 parameters - delta, Px & Py
    ##

    ## cf: http://stackoverflow.com/questions/28237581/closest-pair-implemetation-python
    ## http://rosettacode.org/wiki/Closest-pair_problem


    ## xbar = biggest x-value  in left half of P
    ## Sy = points with x-coordinate in range (x-bar - delta, x-bar + delta), sorted by y-coordinate
    ## initialize variables best = delta, best_pair = null
    ## loop for i = 1: |Sy| -1
    ##  for j - 1:min(7, |Sy| - i)
    ##      compare points p & q - point i and point i+j
    ##      if dist(p,q) < best
    ##          best = dist(p,q); best_pair = (p,q)
    ## return best_pair or null
    print ('best pair ' + str(best_pair))
    return [delta, best_pair]

def test():
    test_list = [(0, 10), (20, 11), (10, 0), (11, 20), (9,9), (11,11)]
    result = brute_force(test_list)
    print ('brute force result: ' + str(result[1]) + '.  Distance is: ' + str(result[0]))
    result2 = closest_pair(test_list)
    print ('closest pair test 1 ' + str(result2))
    test_list2 = [(0, 10), (20, 11), (10, 0), (11, 20), (9,9), (11,11), (44,44), (99,99)]
    print ('closest pair test 2 ' + str(closest_pair(test_list2)))



test()
