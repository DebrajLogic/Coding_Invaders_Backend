def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j+1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr


data = [-2, 45, 0, 11, -9]

sorted_data = bubble_sort(data)

print(sorted_data)
