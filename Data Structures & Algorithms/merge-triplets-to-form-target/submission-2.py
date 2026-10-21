class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set() # set of valid indices (1, 2, 3)
        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(3)): continue
            for idx, value in enumerate(triplet):
                if value == target[idx]: valid.add(idx)
        return len(valid) == 3