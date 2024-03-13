class MyHashtable():
    def __init__(self):
        self.hashtable = dict()

    def put(self, key, value):
        self.hashtable[key] = value

    def remove(self, key):
        self.hashtable.pop(key)

    def delete_item(self, key):
        del self.hashtable[key]

    def display(self):
        print(self.hashtable)
