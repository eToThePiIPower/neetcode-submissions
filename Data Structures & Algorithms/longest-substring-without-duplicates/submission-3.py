class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        maxLen = 0
        for right in range(len(s)):
            if s[right] in visited:
                if right - left > maxLen:
                    maxLen = right - left
                while s[left] != s[right]:
                    visited.remove(s[left])
                    left += 1
                left +=1
            else:
                visited.add(s[right])
        if len(s) - left > maxLen:
            maxLen = len(s) - left
        return maxLen