class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = [None, None, None]
        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(3)): continue
            for i in range(3):
                if triplet[i] == target[i]: merged[i] = triplet[i]
        return merged == target