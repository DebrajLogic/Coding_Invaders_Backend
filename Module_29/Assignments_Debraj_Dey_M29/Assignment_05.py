# Given an array of integers of length n. Our task is to return the index of the max element if it is at least twice as much as every other number in the array. If the max element does not satisfy the condition return -1

'''
Input: arr = {3, 6, 1, 0}
Output: 1
Explanation: Here, 6 is the largest integer, and for every other number in the array x, 6 is more than twice as big as x. The index of value 6 is 1, so we return 1.

Input:   arr = {1, 2, 3, 4}
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Note: You must implement a solution with a linear runtime complexity O(n) and use only constant extra space.
'''

from decorator import output


@output
def find_max_number(nums):
    largest = max(nums)

    for num in nums:
        if num == largest:
            continue
        elif largest >= 2 * num:
            continue
        else:
            return -1

    return nums.index(largest)


arr = [3, 6, 1, 0]
find_max_number(arr)
