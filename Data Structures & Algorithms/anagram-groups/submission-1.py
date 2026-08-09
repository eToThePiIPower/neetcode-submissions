from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = strToKey(s)
            groups[key].append(s)
        return list(groups.values())

def strToKey(s):
    freqs = [0] * 26
    for c in s:
        freqs[ord(c) - 97] += 1
    return tuple(freqs)