
# def partition(array, start, end):
#     pivot = array[start]
#     low = start + 1
#     high = end

#     while True:
#         # If the current value we're looking at is larger than the pivot
#         # it's in the right place (right side of pivot) and we can move left,
#         # to the next element.
#         # We also need to make sure we haven't surpassed the low pointer, since that
#         # indicates we have already moved all the elements to their correct side of the pivot
#         while low <= high and array[high] >= pivot:
#             high = high - 1

#         # Opposite process of the one above
#         while low <= high and array[low] <= pivot:
#             low = low + 1

#         # We either found a value for both high and low that is out of order
#         # or low is higher than high, in which case we exit the loop
#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#             # The loop continues
#         else:
#             # We exit out of the loop
#             break

#     array[start], array[high] = array[high], array[start]

#     return high


def partition(integer_array, start_index, end_index):
    """
    Partitions an array around pivot into two sub arrays

    Args:
    integer_array -- list of integers
    pivot -- element of array at which partition takes place

    Returns:
    a list after the partition around pivot
    """
    pivot = integer_array[start_index]

    i = start_index
    for j in range(start_index, end_index):
        if integer_array[j] < pivot and integer_array[j] != pivot:
            temp = integer_array[i]
            integer_array[i] = integer_array[j]
            integer_array[j] = temp
            i += 1

    temp = integer_array[integer_array.index(pivot)]
    integer_array[integer_array.index(pivot)] = integer_array[i]
    integer_array[i] = temp

    # comparison.append(end_index - start_index)


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


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


array = openfile("algorithm-quicksort.txt")
list_of_string_to_integer(array)
quick_sort(array, 0, len(array) - 1)
print(array)