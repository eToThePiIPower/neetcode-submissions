LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(idx):
            nonlocal current
            if idx >= len(digits):
                if current: results.append(current)
                return
            for c in LETTERS[digits[idx]]:
                current = current + c
                backtrack(idx+1)
                current = current[:-1]
        
        results = []
        current = ""
        backtrack(0)
        return results