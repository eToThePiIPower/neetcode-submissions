class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = [-1] * n
        def dfs(i: int) -> int:
            if i < n and cache[i] != -1: return cache[i]

            if i < n and s[i] == '0': return 0
            elif i >= n - 1: return 1
            elif s[i] >= '3':
                cache[i] = dfs(i+1)
                return cache[i]
            elif s[i] == '1':
                cache[i] = dfs(i+1) + dfs(i+2)
                return cache[i]
            elif s[i] == '2' and s[i+1] <= '6':
                cache[i] = dfs(i+1) + dfs(i+2)
                return cache[i]
            else:
                cache[i] = dfs(i+1)
                return cache[i]
        return dfs(0)