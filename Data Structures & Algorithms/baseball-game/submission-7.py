class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:
            if op == "+":
                newScore = stack[-1] + stack[-2]
            elif op == "C":
                total -= stack.pop()
                continue
            elif op == "D":
                newScore = 2 * stack[-1]
            else:
                newScore = int(op)
                
            stack.append(newScore)
            total += newScore
            
        return total