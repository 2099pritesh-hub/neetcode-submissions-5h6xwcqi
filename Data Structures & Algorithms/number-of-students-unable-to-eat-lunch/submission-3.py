class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        res = len(students)

        for sandwich in sandwiches:
            cnt = 0
            while cnt < len(q) and q[0] != sandwich:
                q.append(q.popleft())
                cnt += 1
            
            if q[0] == sandwich:
                q.popleft()
                res -= 1
            else:
                break
        
        return res