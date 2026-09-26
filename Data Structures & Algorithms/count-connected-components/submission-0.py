class Solution:
    def dfs(self, adjList, visited, source):
        visited[source] = True
        for nei in adjList[source]:
            if not visited[nei]:
                self.dfs(adjList, visited, nei)
        

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            src, dest = edge
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        components = 0
        for i in range(len(visited)):
            if not visited[i]:
                components+=1
                self.dfs(adj_list, visited, i)
        return components

        