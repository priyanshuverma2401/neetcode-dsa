class Solution:
    def detectCycle(self, source, adjList, visited, recursionPath):
        visited[source] = True
        recursionPath[source] = True
        for nei in adjList[source]:
            if not visited[nei]:
                if self.detectCycle(nei, adjList, visited, recursionPath):
                    return True
            if recursionPath[nei]: return True
        recursionPath[source] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        recursionPath = [False for _ in range(numCourses)]

        for ele in prerequisites:
            course, pre = ele[0], ele[1]
            adjList[pre].append(course)
        
        for i in range(len(visited)):
            if not visited[i] and self.detectCycle(i, adjList, visited, recursionPath):
                return False
        return True
        