def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return None

arr = [1, 2, 3, 5, 8, 11]
target = 10
print(two_sum_sorted(arr, target))

# len gives the length of the array

# left = 0 ---> 1
# right = 5 ---> 11
# current_sum = 12

# left = 0 ---> 1
# right = 4 ---> 8
# current_sum = 9

# left = 1 ---> 2
# right = 4 ---> 8
# current_sum = 10
# [1, 4]

