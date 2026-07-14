class Solution:
    def isValid(self, s: str) -> bool:
        closeToopen = {")":"(", "}":"{", "]":"["}
        stack = []

        for b in s:
            if b in closeToopen:
                if not stack or closeToopen[b] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(b)
        return True if not stack else False