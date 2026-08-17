class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left, maxLen = 0, 0

        for right in range(len(s)):
            if s[right] in visited:
                # update the maxLen if needed
                if right - left > maxLen:
                    maxLen = right - left
                # move the left pointer until the matching character
                # under the right pointer is removed
                while s[right] in visited:
                    visited.remove(s[left])
                    left += 1
                visited.add(s[right])
            else:
                visited.add(s[right])
        
        # check the final substring
        if len(s) - left > maxLen:
            maxLen = len(s) - left
        return maxLen