def linear_search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 4
n = len(array)

result = linear_search(array, n, x)

if result == -1:
    print('Not found')
else:
    print(f'Found at index {result}')
