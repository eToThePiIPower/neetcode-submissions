class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [True] + [False] * n
        
        for i in range(1, n+1):
            dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))
        return dp[n]