# Given an array of n integers and given a number K, determines whether there is a pair of elements in the array that sums to exactly K.If found Print the first Pair Found else print No Pairs Found

def find_sum_pairs(integers, sum):
    complements = {}

    for integer in integers:
        complements[integer] = sum - integer

    # print(complements)

    for key, value in complements.items():
        if value in complements:
            return key, value
    return 'No Pairs Found'


# integers = [-5, 1, -40, 20, 6, 8, 7]
# integers = [-5, 4, -2, 16, 8, 9]
# K = 15

array = input()
K = int(input())

array = array.split(' ')
array = [int(x) for x in array]

print(find_sum_pairs(array, K))
