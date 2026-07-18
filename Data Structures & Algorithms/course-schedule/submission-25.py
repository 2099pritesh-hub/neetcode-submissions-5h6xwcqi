class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for src, dst in prerequisites:
            adjList[src].append(dst)
        
        visit = set()

        def dfs(crs):
            if adjList[crs] == []:
                return True
            if crs in visit:
                return False
            
            visit.add(crs)
            for neigh in adjList[crs]:
                if not dfs(neigh):
                    return False
            # visit.remove(crs)
            adjList[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True