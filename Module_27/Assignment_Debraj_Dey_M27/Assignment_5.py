#  Given an array of size n, return the majority element.
# The majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.


def find_majority_element(array):
    elements = {}
    n = len(array)

    for number in array:
        if number in elements:
            elements[number] += 1
        else:
            elements[number] = 1

    # print(elements)

    for element in elements:
        if elements[element] > n / 2:
            return element


results = []
test_cases = int(input())
while (test_cases > 0):
    array = input()
    array = array.split(' ')
    array = [int(x) for x in array]
    results.append(find_majority_element(array))
    test_cases -= 1


for result in results:
    print(result)
