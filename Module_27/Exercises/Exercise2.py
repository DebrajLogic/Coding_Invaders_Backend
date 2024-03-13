# Write a Python program to create a dictionary from a string.
# Track the count of the letters from the string.

from HashTable import MyHashtable

str = 'malayalam'

hashtable = MyHashtable()
for letter in str:
    count = 1
    if letter in hashtable.hashtable:
        count = hashtable.hashtable[letter]
        count += 1
    hashtable.put(letter, count)


hashtable.display()
