"""
    Usage: python algorithm-quicksort.py
"""


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

    # base case
    if end_index - start_index < 2:
        # return (integer_array, num_comparison)
        return

    pivot = choose_pivot(integer_array, start_index, end_index)
    partition(integer_array, start_index, end_index, pivot, comparison)
    partition_index = integer_array.index(pivot)

    # first_partition = partitioned_integer_array[0:partition_index]
    # second_partition = partitioned_integer_array[partition_index:len(partitioned_integer_array)]
    # print(first_partition)
    # print(second_partition)

    run(integer_array, start_index, partition_index, comparison)
    run(integer_array, partition_index+1, len(integer_array), comparison)

    return sum(comparison)


def partition(integer_array, start_index, end_index, pivot, comparison):
    """
    Partitions an array around pivot into two sub arrays

    Args:
    integer_array -- list of integers
    pivot -- element of array at which partition takes place

    Returns:
    a list after the partition around pivot
    """

    i = start_index
    for j in range(start_index, end_index):
        if int(integer_array[j]) < int(pivot) and int(integer_array[j]) != int(pivot):
            temp = integer_array[i]
            integer_array[i] = integer_array[j]
            integer_array[j] = temp
            i += 1

    temp = integer_array[integer_array.index(pivot)]
    integer_array[integer_array.index(pivot)] = integer_array[i]
    integer_array[i] = temp

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

    return integer_array[end_index-1]

    middle = 0
    if len(integer_array) % 2 == 0:
        middle = int(end_index - start_index / 2)
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


# sys.setrecursionlimit(1500)
# print(choose_pivot([3,8,2,5,1,4,7,6], 0, len([3,8,2,5,1,4,7,6])))
# array = openfile("test.txt")
array = openfile("test1.txt")
# array = [5,8,4,7,6]
# array = [3,8,2,5,1,4,7,6]
# array = openfile("algorithm-quicksort.txt")
print(run(array, 0, len(array), []))