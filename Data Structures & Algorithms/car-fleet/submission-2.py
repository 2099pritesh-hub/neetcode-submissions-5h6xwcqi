class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []
        for i in range(len(position)):
            position_speed.append([position[i], speed[i]])
        
        position_speed.sort()

        stack = []
        fleet = 0
        for i in range(len(position_speed) - 1, -1, -1):
            p = position_speed[i][0]
            s = position_speed[i][1]
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
                fleet += 1
        return fleet            