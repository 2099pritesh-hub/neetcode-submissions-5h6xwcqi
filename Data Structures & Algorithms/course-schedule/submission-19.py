class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for src, dst in prerequisites:
            adjList[src].append(dst)

        def dfs(crs, visit):
            if adjList[crs] == []:
                return True
            if crs in visit:
                return False
            

            visit.add(crs)
            for neigh in adjList[crs]:
                if not dfs(neigh, visit):
                    return False
            # visit.remove(crs)
            adjList[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True