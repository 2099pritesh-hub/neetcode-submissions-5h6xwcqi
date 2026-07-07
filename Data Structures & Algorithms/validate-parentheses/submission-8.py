class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "}":"{", "]":"["}
        stack = []

        for b in s:
            if b in closeToOpen:
                if not stack or stack[-1] != closeToOpen[b]:
                    return False
                stack.pop()
            else:
                stack.append(b)

        return len(stack) == 0