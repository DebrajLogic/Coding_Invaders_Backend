videos = [110.5, 145.67, 32.3, 119.28, 7.3, 55.67, 123.4, 11.2, 226.25, 3.9]

count = 0

for video in videos:
    if video > 120:
        count += 1

print(f"No of videos of longer than 2 hours are: {count}")
