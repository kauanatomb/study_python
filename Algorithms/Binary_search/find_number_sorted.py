def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 5, 8, 11]
target = 5
print(binary_search(arr, target))

# left = 0 ---> 1
# right = 5 ---> 11
# mid = 2 ---> 3

# left = 3 ---> 5
# right = 5 ---> 11
# mid = 4 ---> 8

# left = 3 ---> 5
# right = 3 ---> 5
# mid = 3 ---> 5

