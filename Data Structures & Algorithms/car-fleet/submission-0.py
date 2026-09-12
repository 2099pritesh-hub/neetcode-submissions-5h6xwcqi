class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionTime = [[p] for p in position]
        for i in range(len(speed)):
            positionTime[i].append(speed[i])
        positionTime.sort()

        stack = []
        for i in range(len(positionTime) - 1, -1, -1):
            time = (target - positionTime[i][0]) / positionTime[i][1]
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)