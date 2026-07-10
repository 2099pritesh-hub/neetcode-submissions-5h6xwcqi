class Solution:
    def isValid(self, s: str) -> bool:
        closeToopen = {"}":"{", ")":"(", "]":"["}
        stack = []

        for b in s:
            if b in closeToopen:
                if not stack or stack[-1] != closeToopen[b]:
                    return False
                stack.pop()
            else:
                stack.append(b)
        return len(stack) == 0