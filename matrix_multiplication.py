'''approaches to multiplying two SQUARE matrices with identical dimensions
Will throw an error if these conditions are not met'''

## setup stuff
import time

def brute_force(x_matrix, y_matrix):
    '''brute force calculation of matrix multiplication
    assumes 2 square matrices and does not check for this'''
    start = time.time()

    ## create empty output matrix - works for different sizes
    z_matrix = [[0 for dummycol in range(len(x_matrix))]
                           for dummyrow in range(len(y_matrix[0]))]

    for xrow in len(x_matrix):
        for ycol in len(y_matrix[0]):
            for yrow in len(y_matrix):
                z_matrix[x_row, yxol] = 0 ### work this out


    print (time.time() - start)
    return z_matrix

def matrix_multiplication(x_matrix, y_matrix):
    pass

def gen_random_square_matrix(size):
    pass

def test():
    pass
