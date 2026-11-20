class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(s2 - s1)
            elif t == "*":
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(s2 * s1)
            elif t == "/":
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(int(s2 / s1))
            else:
                stack.append(int(t))
        return stack[0]