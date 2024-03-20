# Given an array, find the total number of inversions of it. If (i < j) and (A[i] > A[j]), then pair (i, j) is called an inversion of an array A. We need to count all such pairs in the array.

def count_inversions(arr):
    inversions = []
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if i < j and arr[i] > arr[j]:
                inversions.append((arr[i], arr[j]))

    return len(inversions)


array = [1, 9, 6, 4, 5]
print(f'The inversion count is {count_inversions(array)}')
