'''routine to calculate closest set of pairs in a 2-d plane'''

## setup stuff
import time
import math
import merge_sort_quiz as ms
import matplotlib.pyplot as pyplot
import random


def euc_distance(point1, point2):
    '''returns euclidian distance between 2 points'''
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def brute_force(lst):
    '''double-loop routine to find closest 2 points from a set'''
    closest_distance = float('inf')
    closest_pair = [(), ()]
    for point1 in range(len(lst) - 1):
        for point2 in range(point1 + 1, len(lst)):
            if euc_distance(lst[point1], lst[point2]) < closest_distance:
                closest_distance = euc_distance(lst[point1], lst[point2])
                closest_pair[0] = lst[point1]
                closest_pair[1] = lst[point2]
    return [closest_distance, closest_pair]


def closest_pair(lst):
    '''main function to solve for closest pair among a set of points'''
    x_sort = ms.merge_sort(lst, 0)
    y_sort = ms.merge_sort(lst, 1)
    solution = cp_split(x_sort, y_sort)
    return solution


def cp_split(x_list, y_list):
    '''recursive routine called by closest_pair - takes 2 sorted lists as input'''
    if len(x_list) <= 3:
        return brute_force(x_list)
    else:
        x_left = x_list[:len(x_list) // 2]
        x_right = x_list[len(x_list) // 2:]
        x_bar = x_left[-1][0]
        y_left = [val for val in y_list if val[0] <= x_bar]
        y_right = [val for val in y_list if val[0] > x_bar]
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
    '''solves for closest pair split over two halves of a list'''
    x_bar = x_list[len(x_list) // 2][0]
    y_subset = [val for val in y_list if abs(x_bar - val[0]) < delta]
    best = delta
    for counter1 in range(len(y_subset) - 1):
        for counter2 in range(1, min(counter1 + 7, len(y_subset) - counter1)):
            point1 = y_subset[counter1]
            point2 = y_subset[counter1 + counter2]
            split_dist = euc_distance(point1, point2)
            if split_dist < best:
                best_pair = [point1, point2]
                best = split_dist
    return [best, best_pair]


def test():
    '''testing routine'''
    test_list = [(0, 10), (20, 11), (10, 0), (11, 20), (9, 9), (11, 11)]
    # start = time.time()
    result = brute_force(test_list)
    # print ("brute force time: " + str(time.time() - start))
    print('brute force result: ' + str(result[1]) + '.  Distance is: ' + str(result[0]))

    # start = time.time()
    result2 = closest_pair(test_list)
    # print ('closest pair time: ' + str(time.time() - start))
    print('closest pair results ' + str(result2[1]) + '. Distance is: ' + str(result2[0]))

    test_list2 = [(0, 10), (20, 11), (10, 0), (11, 20), (9, 9), (11, 11), (44, 44), (99, 99)]
    print('closest pair test 2 ' + str(closest_pair(test_list2)))


def generate_random_point_set(set_length, point_range = 10000):
    '''generates a list containing a random set of points in a plane'''
    lst = []
    for ctr in range(set_length):
        lst.append((random.randrange(point_range), random.randrange(point_range)))
    return lst

def plot_performance(upper_limit = 25, increment = 5):
    '''generates a plot comparing run time for brute force and closest_pair approaches'''
    brute_time = []
    algorithm_time = []
    x_values = range(5, upper_limit + 1, increment)
    for test_len in x_values:
        print (test_len)
        lst = generate_random_point_set(test_len)
        start = time.time()
        brute_force(lst)
        brute_time.append(time.time() - start)
        start = time.time()
        closest_pair(lst)
        algorithm_time.append(time.time() - start)
    pyplot.plot(x_values, brute_time, label = 'brute force time')
    pyplot.plot(x_values, algorithm_time, label = 'algorithm time')
    pyplot.legend(loc='upper left')
    pyplot.show()

# test()



plot_performance(2000, 50)