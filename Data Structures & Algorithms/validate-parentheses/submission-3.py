class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")" : "(", "}" : "{", "]" : "["}

        for i in s:
            if i in close_to_open.values():
                stack.append(i)
            else:
                if stack and stack[-1] == close_to_open[i]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0