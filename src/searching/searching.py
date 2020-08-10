# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end < start:
        return -1
    
    middle = (end + start) // 2
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search(arr, target, start, middle - 1)
    else:
        return binary_search(arr, target, middle + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return 0 if (arr[0] == target) else -1
    
    if arr[0] < arr[1]:
        return binary_search(arr, target, 0, len(arr) - 1)
    else:
        return binary_search_descending(arr, target, 0, len(arr) - 1)

def binary_search_descending(arr, target, start, end):
    if end < start:
        return -1
    
    middle = (end + start) // 2
    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binary_search_descending(arr, target, start, middle - 1)
    else:
        return binary_search_descending(arr, target, middle + 1, end)