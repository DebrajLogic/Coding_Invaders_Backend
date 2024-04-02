# Problem Statement:
# We have been given a number Let’s say n.

# You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your apartment, you want to optimise its location.

# You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment. The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question.

# For instance, for every block, you might know whether a school, a pool, an office, and a gym are present or not. In order to optimise your life, you want to minimise the farthest distance you'd have to walk from your apartment to reach all of your required buildings.

# Write a function that takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that is most optimal for you.
from decorator import output


@output
def apartment_hunting(blocks, reqs):
    pass


input_arr = [
    {"gym": False, "school": True, "store": False, },
    {"gym": True, "school": False, "store": False, },
    {"gym": True, "school": True, "store": False, },
    {"gym": False, "school": True, "store": False, },
    {"gym": False, "school": True, "store": True, }
]

reqs = ["gym", "school", "store"]


apartment_hunting(input_arr, reqs)
