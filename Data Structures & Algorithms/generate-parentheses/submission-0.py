class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def backtrack(count_left: int, count_right: int, current: str) -> None:
            # base cases: invalid paren numbers and finished parens
            if count_left > n or count_right > n or count_left < count_right: return
            if count_left == n and count_right == n:
                results.append(current)
                return
            
            # try adding a left parens
            backtrack(count_left + 1, count_right, current + "(")
            # now try adding a right parens
            backtrack(count_left, count_right + 1, current + ")")
        
        backtrack(0, 0, "")

        return results