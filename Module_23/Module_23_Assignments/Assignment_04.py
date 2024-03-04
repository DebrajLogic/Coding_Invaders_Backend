videos = {'Tuple in Python': [13.0, 134.5, 89.3, 98.4],
          'Lists in Python': [72.0, 83.5, 90.3, 98.4],
          'Dictionary in Python': [41.0, 114.5, 62.3, 198.4]}


def longest_play_time(videos):
    longest_play_time = 0

    for play_time in videos:
        if play_time > longest_play_time:
            longest_play_time = play_time
    return longest_play_time


for key, value in videos.items():
    print(longest_play_time(value), end=' ')
