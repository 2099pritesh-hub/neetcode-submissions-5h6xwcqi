class Solution:
    def isValid(self, s: str) -> bool:
        closeToopen = {')':'(', ']':'[', '}':'{'}
        stack = []

        for b in s:
            if b in closeToopen:
                if stack and stack[-1] == closeToopen[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return not stack