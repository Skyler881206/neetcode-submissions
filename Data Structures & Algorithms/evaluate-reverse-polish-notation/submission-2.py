class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                 stack.append(int(token)) # Get the value
            else:
                value = stack.pop()
                valued = stack.pop()

                if token == "+":
                    stack.append(valued + value)
                
                elif token == "-":
                    stack.append(valued - value)

                elif token == "*":
                    stack.append(valued * value)
                
                elif token == "/":
                    stack.append(int(valued / value))
        return stack[0]