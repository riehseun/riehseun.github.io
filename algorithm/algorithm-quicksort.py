"""
Usage: python algorithm-quicksort.py
"""


import resource
import sys


def run(integer_array, start_index, end_index, comparison):
    """
    Implements quicksort and computes # of comparison in partition subroutine

    Args:
    integer_array -- list of integers
    file -- string representing location of files containing lots of number

    Retunrs:
    Tuple of list representing sorted array and an integer representing the number of comparison in partition subroutine
    """

    # base case: there is only 1 element in the array to sort
    if end_index <= start_index:
        return

    pivot = choose_pivot(integer_array, start_index, end_index)
    partition(integer_array, start_index, end_index, pivot, comparison)
    partition_index = integer_array.index(pivot)

    run(integer_array, start_index, partition_index-1, comparison)
    run(integer_array, partition_index+1, len(integer_array)-1, comparison)

    # print(len(comparison))
    #print(integer_array)
    #return sum(comparison)
    # return integer_array


def partition(integer_array, start_index, end_index, pivot, comparison):
    """
    Partitions an array around pivot into two sub arrays

    Args:
    integer_array -- list of integers
    pivot -- element of array at which partition takes place

    Returns:
    a list after the partition around pivot
    """

    i = start_index + 1
    for j in range(start_index + 1, end_index+1):
        if integer_array[j] < pivot:
            temp = integer_array[i]
            integer_array[i] = integer_array[j]
            integer_array[j] = temp
            i += 1

    # temp = integer_array[integer_array.index(pivot)]
    # integer_array[integer_array.index(pivot)] = integer_array[i]
    # integer_array[i] = temp
    temp = integer_array[start_index]
    integer_array[start_index] = integer_array[i-1]
    integer_array[i-1] = temp

    comparison.append(end_index - start_index)


def choose_pivot(integer_array, start_index, end_index):
    """
    Choose a pivot elemnet from input list

    Args:
    integer_array -- list of integers

    Retunrs:
    Tuple of an integer and an index representing the pivot
    """

    # return integer_array[start_index]

    return integer_array[end_index]

    middle = 0
    if len(integer_array) % 2 == 0:
        middle = int((end_index - start_index) / 2)
    else:
        middle = int(len(integer_array) / 2)

    num1 = integer_array[start_index]
    num2 = integer_array[end_index-1]
    num3 = integer_array[middle]

    median=0
    if num1>num2:
        if num1<num3:
            median= num1
        elif num2>num3:
            median= num2
        else:
            median= num3
    else:
        if num1>num3:
            median= num1
        elif num2<num3:
            median= num2
        else:
            median= num3
    return median


def openfile(file_path):
    """

    """
    with open(file_path, 'r') as line:
        integer_array = line.read().split("\n")
    return integer_array


def list_of_string_to_integer(input_list):
    """

    """
    for i in range(0, len(input_list)):
        input_list[i] = int(input_list[i])


array_test1 = [5,8,4,7,6]
partition(array_test1, 0, len(array_test1)-1, 5, [])
assert(array_test1 == [4,5,8,7,6])
array_test2 = [3,8,2,5,1,4,7,6]
partition(array_test2, 0, len(array_test2)-1, 3, [])
assert(array_test2 == [1,2,3,5,8,4,7,6])


resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
sys.setrecursionlimit(10000)
# print(choose_pivot([3,8,2,5,1,4,7,6], 0, len([3,8,2,5,1,4,7,6])))
array = openfile("algorithm-quicksort.txt")
# array = [54044,14108,79294,29649,25260,60660,2995,53777,49689,9083,16122,90436,4615,40660,25675,58943,92904]
# array = [3,8,2,5,1,4,7,6]
# array = [3,8,2,5,1,4,7,6,10,9]
list_of_string_to_integer(array)
print(run(array, 0, len(array)-1, []))
print(array)

# Increase stack size?