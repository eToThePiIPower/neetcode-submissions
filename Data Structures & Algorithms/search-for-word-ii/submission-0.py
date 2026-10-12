class Trie:
    def __init__(self):
        self.children: List[Optional['Trie']] = [None] * 26
        self.word_idx = -1
    def insert(self, word: str, idx: int) -> None:
        """ Insert a word into the prefix list pointing to source index"""
        curr = self
        for c in word:
            char_idx = ord(c) - ord('a')
            if curr.children[char_idx] is None: curr.children[char_idx] = Trie()
            curr = curr.children[char_idx]
        # marks the end of a word with it's source index
        curr.word_idx = idx

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(x: int, y: int, node: Trie) -> None:
            # invalid x,y or cell already visited
            if not 0 <= x < len(board) or not 0 <= y < len(board[0]): return
            if board[x][y] == ".": return

            # Move to the new node
            char_idx = ord(board[x][y]) - ord('a')
            if node.children[char_idx] is None: return
            node = node.children[char_idx]

            # Check for word completion
            if node.word_idx >= 0:
                results.append(words[node.word_idx])
                node.word_idx = -1
            
            # mark cell as visited, backtrack, then restore cell
            char, board[x][y] = board[x][y], "."
            backtrack(x-1, y, node)
            backtrack(x+1, y, node)
            backtrack(x, y-1, node)
            backtrack(x, y+1, node)
            board[x][y] = char
        
        trie = Trie()
        for idx, word in enumerate(words): trie.insert(word, idx)

        results = []
        for x in range(len(board)):
            for y in range(len(board[0])):
                backtrack(x, y, trie)

        return results