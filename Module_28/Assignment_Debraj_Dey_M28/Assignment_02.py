# Given a sorted array consisting of N distinct integers and an integer K, the task is to find the index of K, if it’s present in the array.
# We need to find the index where K must be inserted to keep the array sorted.

def find_index(arr, element):
    for i in range(0, len(arr)):
        if element == arr[i]:
            return i
        elif arr[i] < element < arr[i+1]:
            return i + 1
        else:
            continue


array = input('Enter array elements separated by comma: ')
array = array.split(',')
array = [int(element) for element in array]
K = int(input('Enter the element to be inserted: '))
print(find_index(array, K))
