class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n == 1:
            return int(tokens[0])

        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(token)
                continue
            right = int(stack.pop())
            left = int(stack.pop())

            op = token

            if op == '+':
                val = left + right
            elif op == '-':
                val = left - right
            elif op == '*':
                val = left * right
            else:
                val = int(left / right)
            
            stack.append(str(val))
        
        return int(stack[0])

        # T = O(n)
        # S = O(n)
        