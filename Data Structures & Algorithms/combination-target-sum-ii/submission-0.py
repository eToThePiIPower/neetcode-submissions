class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        current_combination = []

        def backtrack(start_idx: int, remaining: int) -> None:
            # Base successand and failure cases
            if remaining == 0:
                # [:] creates a shallow copy instead of reference
                results.append(current_combination[:])
                return
            if start_idx >= len(candidates) or remaining < 0:
                return

            for idx in range(start_idx, len(candidates)):
                if idx > start_idx and candidates[idx] == candidates[idx - 1]:
                    continue
                current_combination.append(candidates[idx])
                backtrack(idx + 1, remaining - candidates[idx])
                current_combination.pop()
            
        backtrack(0, target)
        return results