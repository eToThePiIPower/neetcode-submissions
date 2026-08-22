class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetFreqs = self.__freqsFor(t)
        subFreqs = {}

        left = 0
        minSubString = ""

        for right in range(len(s)):
            subFreqs[s[right]] = subFreqs.get(s[right], 0) + 1
            if self.__contains(subFreqs, targetFreqs):
                while (
                    not s[left] in targetFreqs
                    or subFreqs[s[left]] > targetFreqs[s[left]]
                ):                
                    subFreqs[s[left]] -= 1
                    left += 1
                if not minSubString or len(minSubString) > len(s[left:right+1]):
                    minSubString = s[left:right+1]
        
        return minSubString
        
            
    
    def __freqsFor(self, s: str) -> dict[str, int]:
        freqs = {}
        for char in s:
            freqs[char] = freqs.get(char, 0) + 1
        return freqs
    
    def __contains(self, string: dict, target: dict) -> bool:
        for k, v in target.items():
            if k not in string:
                return False
            if v > string[k]:
                return False
        return True