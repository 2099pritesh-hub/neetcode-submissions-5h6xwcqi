class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for src, dst in prerequisites:
            adjList[src].append(dst)
        
        visit = set()
        
        def dfs(c):
            if adjList[c] == []:
                return True
            if c in visit:
                return False
            
            visit.add(c)
            for neigh in adjList[c]:
                if not dfs(neigh):
                    return False
            visit.remove(c)
            adjList[c] = []
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True