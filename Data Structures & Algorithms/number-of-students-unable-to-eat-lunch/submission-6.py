class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hashMap = {0:0, 1:0}
        for s in students:
            hashMap[s] += 1
        
        res = len(students)
        for s in sandwiches:
            if hashMap[s] > 0:
                res -= 1
                hashMap[s] -= 1
            else:
                return res
        return res