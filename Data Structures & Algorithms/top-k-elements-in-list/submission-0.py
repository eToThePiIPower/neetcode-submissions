from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        sorted_freqs = [k for k, v in sorted(freqs.items(), key = lambda i: -i[1])]
        return sorted_freqs[:k]
