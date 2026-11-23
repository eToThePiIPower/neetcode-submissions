class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            l = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:l] == w2[:l]:
                return "" # invalid; abcd cannot come before abc
            for j in range(l):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = {} # True == visited and in current path
        res = []

        def dfs(c):
            if c in visited:
                return visited[c] # if True, loop detected
            visited[c] = True

            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True

            visited[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
