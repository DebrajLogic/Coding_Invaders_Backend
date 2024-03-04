video = ["List in Python", [34.5, 19.2, 381.3, 56.2, 16.1]]

list_to_sort = video[1]

for i in range(0, len(list_to_sort)):
    for j in range(0, len(list_to_sort) - i - 1):
        if (list_to_sort[j] > list_to_sort[j+1]):
            temp = list_to_sort[j+1]
            list_to_sort[j+1] = list_to_sort[j]
            list_to_sort[j] = temp

print(list_to_sort)
