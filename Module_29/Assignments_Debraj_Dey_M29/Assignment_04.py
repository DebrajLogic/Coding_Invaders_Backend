# In Addition to the above problem, solve the same using a solution with a linear runtime complexity O(n) and use only constant extra space.
# Hint: Try to Google about XOR

from decorator import output


@output
def find_single_number(nums):
    # counter = {}

    # for num in nums:
    #     if num in counter:
    #         counter[num] += 1
    #     else:
    #         counter[num] = 1

    # for key, value in counter.items():
    #     if value == 1:
    #         return key

    result = 0
    for num in nums:
        result = result ^ num
    return result


arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9]
find_single_number(arr)
