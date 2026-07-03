class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for src, dst in prerequisites:
            adjList[src].append(dst)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            if adjList[node] == []:
                return True

            visit.add(node)
            for neigh in adjList[node]:
                if not dfs(neigh):
                    return False
            visit.remove(node)
            adjList[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True