class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False

    def contains(self, char):
        return True if self.links[ord(char) - ord('a')] else False

    def addLink(self, node, char):
        self.links[ord(char) - ord('a')] = node
        return
    


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if not node.contains(char):
                newNode = Node()
                node.addLink(newNode, char)
                node = newNode
            else:
                node = node.links[ord(char) - ord('a')]
        node.flag = True

    def search(self, word: str) -> bool:
        node =  self.root
        for i in range(len(word)):
            if not node.contains(word[i]):
                return False
            node = node.links[ord(word[i]) - ord('a')]
        if node.flag : return True
        return False
        

    def startsWith(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if not node.contains(word[i]): return False
            node = node.links[ord(word[i]) - ord('a')]
        return True
        
        