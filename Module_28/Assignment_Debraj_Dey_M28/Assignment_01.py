# There is  a school called ABC, in which 5th Class students are mischievous. Teacher had the list of students roll no’s, Some students they have done mischief in that list they are adding proxies of their friends , due to which in the list there is duplicate roll numbers now,Now Teacher have to find the repeated roll numbers, We have to help teach to find the duplicate and repeated roll numbers.

def find_repeat_numbers(arr):
    repeats = {}

    for number in arr:
        if number in repeats:
            repeats[number] += 1
        else:
            repeats[number] = 1

    for number in repeats:
        if repeats[number] > 1:
            print(number)


roll_numbers = [11, 21, 19, 34, 19, 23, 24, 22, 25, 22, 21, 11, 31]
