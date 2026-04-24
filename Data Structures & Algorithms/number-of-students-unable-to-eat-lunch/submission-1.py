class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsPreference = {}

        for i in students:
            studentsPreference[i] = studentsPreference.get(i, 0) + 1
        
        for s in sandwiches:
            if studentsPreference.get(s, 0):
                studentsPreference[s] -= 1
            else:
                return sum(studentsPreference.values())
        
        return sum(studentsPreference.values())