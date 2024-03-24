# Write a Program to search for the insert position of a key in an array and print the index of it. if the key is not found, find the index where the key must be inserted to keep the array sorted.
'''
Input: arr[] = {11, 14, 15, 17, 21, 34}, key = 17
Output: 3
Explanation: Since 17 is found at index 3 as arr[3] = 17, the output is 3.

Input: arr[] = {11, 14, 15, 17, 21, 34}, key = 27
Output: 5
Explanation: Since 27 is not present in the array but can be inserted at index 5 to keep the array sorted.
Solve the above problem with O(n) as Time complexity
'''
from decorator import output


@output
def search_position(arr, key):
    if key in arr:
        for i in range(0, len(arr)):
            if key == arr[i]:
                return i
    else:
        for i in range(0, len(arr)):
            if arr[i] > key:
                return i
        return len(arr)


arr = [11, 14, 15, 17, 21, 34]
key = 27

search_position(arr, key)
