Channels = ["Indie Folk Central", "RoadTravelledLess", "Netflix",
            "PlayStation", "RoadTravelledLess", "Python is Awesome", "JavaScript"]


def find_channel_name_violators(channels):

    for channelName in channels:
        if len(channelName) > 15:
            print(channelName)


find_channel_name_violators(Channels)
