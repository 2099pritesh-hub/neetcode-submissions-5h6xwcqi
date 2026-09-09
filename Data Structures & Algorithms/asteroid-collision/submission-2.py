class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            elif a < 0:
                if not stack or stack[-1] < 0:
                    stack.append(a)
                else:
                    flag = True
                    while flag and stack:
                        a1 = stack.pop()
                        if a1 > 0 and a1 < abs(a):
                            if not stack or stack[-1] < 0:
                                stack.append(a)
                                flag = False
                            continue
                        elif a1 < 0:
                            stack.append(a1)
                            stack.append(a)
                            flag = False
                        elif a1 > abs(a):
                            stack.append(a1)
                            flag = False
                        elif a1 == abs(a):
                            flag = False
        return stack