class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        current_partition: List[str] = []
        results: List[List[str]] = []

        def backtrack(start_idx: int) -> None:
            if start_idx == n: # reached the end, append
                results.append(current_partition[:])
                return
            for end_idx in range(start_idx, n):
                current_string = s[start_idx:end_idx+1]
                if current_string == current_string[::-1]:
                    current_partition.append(current_string)
                    backtrack(end_idx + 1)
                    current_partition.pop()
        
        backtrack(0)
        return results
        
