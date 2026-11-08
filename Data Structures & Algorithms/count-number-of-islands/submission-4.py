class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        rows_count, cols_count = len(grid), len(grid[0])
        visited = [[False for _ in range(cols_count)] for _ in range(rows_count)]


        def dfs(r, c):
            stack = collections.deque()
            stack.append((r, c))
            visited[r][c] = True
            while stack:
                rw, cl = stack.pop()
                # adding upper block
                if rw-1 >= 0 and grid[rw-1][cl] == "1" and not visited[rw-1][cl]:
                    stack.append((rw-1, cl))
                    visited[rw-1][cl] = True
                # adding lower block
                if rw + 1 < rows_count and grid[rw+1][cl] == "1" and not visited[rw+1][cl]:
                    stack.append((rw+1, cl))
                    visited[rw+1][cl] = True
                # adding left block
                if cl-1 >= 0 and grid[rw][cl-1] == "1" and not visited[rw][cl-1]:
                    stack.append((rw, cl-1))
                    visited[rw][cl-1] = True
                # adding right block
                if cl+1 < cols_count and grid[rw][cl+1] == "1" and not visited[rw][cl+1]:
                    stack.append((rw, cl+1))
                    visited[rw][cl+1] = True
                    
                    



        for r in range(rows_count):
            for c in range(cols_count):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    island+=1
        return island
        