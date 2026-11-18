class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for o in operations:
            if o == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
                res += score
            elif o == "C":
                res -= stack[-1]
                stack.pop()
            elif o == "D":
                score = 2 * stack[-1]
                stack.append(score)
                res += score
            else:
                score = int(o)
                stack.append(score)
                res += score
        return res