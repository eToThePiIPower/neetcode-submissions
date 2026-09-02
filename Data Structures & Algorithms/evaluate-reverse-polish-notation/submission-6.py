class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x + y)
                if token == "-":
                    stack.append(x - y)
                if token == "*":
                    stack.append(x * y)   
                if token == "/":
                    stack.append(int(float(x) / y))
        return stack[0]
        

            