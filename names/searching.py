# STRETCH: implement Linear Search
def linear_search(arr, target):

  # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    midpoint = len(arr) // 2

    # TO-DO: add missing code
    while low < high:
        if arr[midpoint] == target:
            return midpoint
        if arr[midpoint] > target:
            high = midpoint
            midpoint = (high+low)//2
        else:
            low = midpoint
            midpoint = (high+low)//2

    return -1  # not found

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if arr[middle] == target:
        return middle
    if arr[middle] > target:
        return binary_search_recursive(arr[:middle], target, low, middle)
    else:
        return binary_search_recursive(arr[middle:], target, middle, high)
