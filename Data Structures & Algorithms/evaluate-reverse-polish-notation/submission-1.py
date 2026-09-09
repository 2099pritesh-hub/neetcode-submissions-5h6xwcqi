class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i2 - i1)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(int(i2 / i1))
            else:
                stack.append(int(t))
        return stack[0]
