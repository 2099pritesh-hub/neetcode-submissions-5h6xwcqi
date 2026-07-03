class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        for src, dst in prerequisites:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            if node not in adjList:
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