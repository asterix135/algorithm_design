'''routine to calculate closest set of pairs in a 2-d plane'''

## setup stuff
import time
import math

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
    pass

def test():
    test_list = [(0, 10), (20, 11), (10, 0), (11, 20), (9,9), (11,11)]
    result = brute_force(test_list)
    print ('closest pair is: ' + str(result[0]) + '.  Distance is: ' + str(result[1]))

test()
