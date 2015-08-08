import dsort
import random
import rselect

def random_test(array_len):
    """Test on randomized array"""
    random.seed(0)
    input_array = random.sample(range(array_len), array_len)
    input_array2 = list(input_array)
    i_element = array_len // 2
    print("algorithm result")
    print(dsort.dselect(input_array, i_element))
    print('rselect results')
    print(rselect.rselect(input_array2, i_element))
    print('midpoint')
    print(array_len//2)

def random_test_battery():
    for i in range(5,5006,1000):
        print("array length: " + str(i))
        random_test(i)
        print()

random_test_battery()