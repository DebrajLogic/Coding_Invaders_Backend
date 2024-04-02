# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

from decorator import output


@output
def find_repeat(s):
    counter = {}
    for letter in s:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1

        if counter[letter] == 2:
            return letter


s = "abccbaacz"
find_repeat(s)
