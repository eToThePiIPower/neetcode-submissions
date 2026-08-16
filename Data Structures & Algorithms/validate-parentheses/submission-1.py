class Solution:
    from collections import deque

    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            elif not stack: # stack is empty with a closing bracket
                return False
            else: # Test the closing bracket for matches
                last_char = stack.pop()
                if char == ")" and last_char == "(":
                    continue
                if char == "]" and last_char == "[":
                    continue
                if char == "}" and last_char == "{":
                    continue
                return False
        if not stack:
            return True
        else:
            return False