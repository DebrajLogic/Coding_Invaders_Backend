# In Addition to above problem , Solve the above same problem but the solution time complexity should be O(log n)


from decorator import output


@output
def search_position_quick(arr, key):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end)//2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return start


arr = [11, 14, 15, 17, 21, 34]
key = 17
search_position_quick(arr, key)
