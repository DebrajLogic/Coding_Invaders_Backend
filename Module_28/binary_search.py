def binary_search(arr, n, x):
    low = 0
    high = n
    i = 1
    while low <= high:
        print(f'\n Iteration {i}')
        i += 1
        print(f'low = {arr[low]}, high = {arr[high]}')
        mid = (low + high)//2
        print(f'mid = {arr[mid]}')
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 9
n = len(array) - 1

result = binary_search(array, n, x)
if result == -1:
    print('Not found')
else:
    print(f'Found at index {result}')
