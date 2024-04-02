# Problem Statement
# Given an array arr[ ] with N elements, the task is to find out the longest subarray which has the shape of a mountain.

# A mountain sub-array consists of elements that are initially in ascending order until a peak element is reached and beyond the peak element all other elements of the sub-array are in decreasing order.

from decorator import output


@output
def longestMountain(arr):
    if len(arr) < 3:
        return 0

    max_length = 0

    for i in range(1, len(arr) - 1):
        if arr[i-1] < arr[i] > arr[i+1]:
            left = right = i

            while left > 0 and arr[left-1] < arr[left]:
                left -= 1

            while right < len(arr) and arr[right] > arr[right + 1]:
                right += 1

            length = right - left + 1

            max_length = max(max_length, length)

    return max_length


arr = [2, 1, 4, 7, 3, 2, 5]
longestMountain(arr)
