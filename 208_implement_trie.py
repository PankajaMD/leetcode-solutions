class TrieNode:
    def __init__(self):
        self.R = 26
        self.links = [None] * self.R
        self.isEnd = False

    def containsKey(self, ch: str) -> bool:
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch: str):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch: str, node) -> None:
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self) -> None:
        self.isEnd = True

    def getEnd(self) -> bool:
        return self.isEnd
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for currentChar in word:
            if not node.containsKey(currentChar):
                node.put(currentChar, TrieNode())
            node = node.get(currentChar)
        node.setEnd()

    def searchPrefix(self, word: str):
        node = self.root
        for currentChar in word:
            if node.containsKey(currentChar):
                node = node.get(currentChar)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.getEnd()

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
