class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {s[0]: 1}
        longest, right, left = 1, 0, 0
        for right in range(1, len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            if max(freqs.values()) + k >= right - left + 1:
                longest = max(right - left + 1, longest)
            else:
                freqs[s[left]] -= 1
                left += 1
        return longest