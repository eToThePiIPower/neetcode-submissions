class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            idx = ord(c) - 97
            if curr.children[idx] is None:
                curr.children[idx] = PrefixTree()
            curr = curr.children[idx]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            idx = ord(c) - 97
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            idx = ord(c) - 97
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return True
        
        