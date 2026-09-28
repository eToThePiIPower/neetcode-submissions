class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None: curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.endOfWord = True      

    def search(self, word: str) -> bool:
        def dfs(start_idx: int, node: TrieNode):
            curr = node
            for idx in range(start_idx, len(word)):
                char = word[idx]

                if char == '.':
                    for child in curr.children:
                        if child and dfs(idx+1, child): return True
                    return False

                else:
                    char_idx = ord(char) - ord('a')
                    if curr.children[char_idx] == None: return False
                    curr = curr.children[char_idx]
            return curr.endOfWord

        return dfs(0, self.root)