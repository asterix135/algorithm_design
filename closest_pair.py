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
    return [closest_pair, closest_distance]


def closest_pair(lst):
    start = time.time()
    list_x_sort = ms.merge_sort(lst, 0)
    list_y_sort = ms.merge_sort(lst, 1)


    ## Approach
    ## merge-sort list by x-coordinate (Px)
    ## merge-sort list by y-coordinate (Py)

    ## divide and conquer the main list:
    ## Q = left half/ R = right half
    ## base case = 2 or 3 points
    ## form Qx Qy, Rx Ry (somehow use Px & Py - linear time)
    ## get closest pair in each half (p1, q1) = closest in Q; (p2, q2) = closest in R
    ## calculate delta - min of dist(p1, q1) and dist(p2, q2)
    ## calculate closest split pair (p3, q3) & return closest of (p1, q1), (p2, q2) and (p3, q3)
    ## closest split pair takes 3 parameters - delta, Px & Py
    ##
    ## Closest Split Pair logic
    ## xbar = biggest x-value  in left half of P
    ## Sy = points with x-coordinate in range (x-bar - delta, x-bar + delta), sorted by y-coordinate
    ## initialize variables best = delta, best_pair = null
    ## loop for i = 1: |Sy| -1
    ##  for j - 1:min(7, |Sy| - i)
    ##      compare points p & q - point i and point i+j
    ##      if dist(p,q) < best
    ##          best = dist(p,q); best_pair = (p,q)
    ## return best_pair or null

    print ("closest pair run time: " + str(time.time() - start))
    return None

def cp_split(lst):
    if len(lst) == 2:
        return (lst[0], lst[1])
    elif len(lst) == 3:
        dist1 = euc_distance(lst[0], lst[1])
        dist2 = euc_distance(lst[0], lst[2])
        dist3 = euc_distance(lst[1], lst[2])
        if min(dist1, dist2, dist3) == dist1:
            return (lst[0], lst[1])
        elif min(dist2, dist3) == dist2:
            return (lst[0], lst[2])
        else:
            return (lst[1], lst[2])
    else:
        left_closest = cp_split(lst[:len(lst)//2])
        right_closest = cp_split(lst[len(lst//2):])
        split_closest = closest_split_pair(lst[:len(lst)//2, lst[len(lst)//2 :]])
        return min(left_closest, right_closest, split_closest)

def closest_split_pair(lst1, lst2):
        return None

def test():
    test_list = [(0, 10), (20, 11), (10, 0), (11, 20), (9,9), (11,11)]
    result = brute_force(test_list)
    print ('closest pair is: ' + str(result[0]) + '.  Distance is: ' + str(result[1]))
    result2 = closest_pair(test_list)
    print (result2)



test()
