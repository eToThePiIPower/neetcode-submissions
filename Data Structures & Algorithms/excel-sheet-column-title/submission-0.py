class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []

        while columnNumber > 0:
            columnNumber -= 1
            remainer = columnNumber % 26
            title.append(chr(ord('A') + remainer))
            columnNumber //= 26
        
        return ''.join(reversed(title))