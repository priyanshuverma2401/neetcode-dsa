class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashset = [Node(0) for _ in range(10 ** 4)]
        

    def add(self, key: int) -> None:
        index = key % (10**4)

        head = self.hashset[index]
        while head.next:
            if head.next.key == key:
                return
            head = head.next
        
        head.next = Node(key)
        return
        

    def remove(self, key: int) -> None:
        index = key % (10 ** 4)
        head = self.hashset[index]

        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return 
            head = head.next
        
        return

        

    def contains(self, key: int) -> bool:
        index = key % (10**4)
        head = self.hashset[index]

        while head.next:
            if head.next.key == key: return True
            head = head.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)