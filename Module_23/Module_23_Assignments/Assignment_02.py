videoTuple = ('Tuple in Python', [13.0, 134.5, 89.3, 98.4])

longest_play_time = 0

for play_time in videoTuple[1]:
    if play_time > longest_play_time:
        longest_play_time = play_time

print(longest_play_time)
