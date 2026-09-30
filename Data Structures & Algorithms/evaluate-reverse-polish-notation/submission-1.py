class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for c in tokens:
            if c in {"+", "-", "*", "/"}:
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    res = b+a
                elif c == '-':
                    res = b-a
                elif c == '*':
                    res = b*a
                elif c == '/':
                    res = int(b/a)
                stack.append(res)
                
            else:
                stack.append(int(c))
                
        return stack[-1]
        