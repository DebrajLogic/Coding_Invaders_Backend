# Problem Statement
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
from decorator import output


@output
def two_sum(nums, target):
    complements = {}

    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in complements:
            return [i, nums.index(complement)]
        else:
            complements[nums[i]] = complement


two_sum([3, 2, 4], 6)
