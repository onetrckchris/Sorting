def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                arr[smallest_index], arr[j] = arr[j], arr[smallest_index]
    return arr

# def selection_sort( arr ):
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index

#         for j in range(cur_index + 1, len(arr)):
#             if arr[j] < arr[smallest_index]:
#                 smallest_index = j

#         temp = arr[smallest_index]
#         arr[smallest_index] = arr[cur_index]
#         arr[cur_index] = temp

#     return arr

def bubble_sort( arr ):
    # Starting at 0 will not break the algorithm, however there's no reason to
    # check the first index since it'll never be greater than itself. As such,
    # starting at index 1 is more slightly more efficient.
    swap = True

    while swap:
        swap = False
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr