class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
                sum += stack[-1]
            elif op == "C":
                sum -= stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
                sum += stack[-1]
            else:
                newScore = int(op)
                stack.append(newScore)
                sum += newScore
        return sum