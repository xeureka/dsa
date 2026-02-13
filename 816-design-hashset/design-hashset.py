class MyHashSet:

    def __init__(self):
        self.my_set = set()
        

    def add(self, key: int) -> None:
        self.my_set.add(key)
        

    def remove(self, key: int) -> None:
        self.my_set.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.my_set

