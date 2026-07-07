class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "}":"{", "]":"["}
        stack = []

        for b in s:
            if b in closeToOpen:
                if not stack:
                    return False
                else:
                    if stack[-1] == closeToOpen[b]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(b)

        return True if not stack else False 