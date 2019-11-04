def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                arr[smallest_index], arr[j] = arr[j], arr[smallest_index]
    return arr

def bubble_sort( arr ):
    # Starting at 0 will not break the algorithm, however there's no reason to
    # check the first index since it'll never be greater than itself. As such,
    # starting at index 1 is more slightly more efficient.
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

test_array = [7, 1, 4, 10, -23, 9]
print(bubble_sort(test_array))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr