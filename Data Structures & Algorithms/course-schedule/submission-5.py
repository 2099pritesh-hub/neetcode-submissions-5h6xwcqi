class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        for i in range(numCourses):
            adjList[i] = []

        for src, dst in prerequisites:
            adjList[src].append(dst)
        
        def dfs(n, visit):
            if n in visit:
                return False
            
            visit.add(n)
            for neighbor in adjList[n]:
                if not dfs(neighbor, visit):
                    return False
            visit.remove(n)
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True