videos = [10.5, 45.67, 32.3, 9.28, 7.3, 55.67, 123.4, 11.2, 6.25, 3.9]

# Find the longest running video
longestRunningVideo = videos[0]

for video in videos:
    if video > longestRunningVideo:
        longestRunningVideo = video


print(f"The longest running video is of duration: {longestRunningVideo}")
