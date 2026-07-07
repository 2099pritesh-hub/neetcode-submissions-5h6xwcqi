class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 
        total = 0

        for op in operations:
            if op == "+":
                total += stack[-2] + stack[-1]
                stack.append(stack[-2] + stack[-1])
            elif op == "C":
                total -= stack[-1]
                stack.pop()
            elif op == "D":
                total += 2 * stack[-1]
                stack.append(2 * stack[-1])
            else:
                total += int(op)
                stack.append(int(op))
        return total