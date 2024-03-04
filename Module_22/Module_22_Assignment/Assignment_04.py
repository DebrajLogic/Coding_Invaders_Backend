channels = ["Indie Folk", "RoadTravelled",
            "MusicStation", "Python", "JavaScript"]
keywords = ['Music', 'song', 'folk']


def find_music_channels(channels, keywords):
    music_channels = []
    for channel in channels:
        for keyword in keywords:
            if keyword.lower() in channel.lower():
                music_channels.append(channel)

    return music_channels


print(find_music_channels(channels, keywords))
