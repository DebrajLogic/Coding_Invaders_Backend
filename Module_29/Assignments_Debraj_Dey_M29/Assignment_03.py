# Given an array of integers. All numbers occur twice except one number which occurs once. Find the number in O(n²) time & constant extra space.

from decorator import output


@output
def find_single_number(nums):
    for i in range(0, len(nums)):
        flag = False
        for j in range(0, len(nums)):
            if i != j and nums[i] == nums[j]:
                flag = True
                break

        if not flag:
            return nums[i]


arr = [4, 3, 2, 4, 1, 3, 2]
find_single_number(arr)
