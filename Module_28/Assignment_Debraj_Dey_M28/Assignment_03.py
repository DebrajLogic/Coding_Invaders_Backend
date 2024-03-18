# Given a list of numbers, we need to sort the list of numbers using bubble sort and print the no of swaps required to sort the list in ascending order

def count_swaps(arr):
    count = 0
    for i in range(0, len(arr)):

        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                count += 1
                print(count, arr)
    return count


array = [8, 5, 1, 2]
print(count_swaps(array))
