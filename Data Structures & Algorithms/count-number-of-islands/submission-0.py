class Solution:
    def dfs(self, grid, visited, r, c, rows, cols):

        if (
            r < 0 or
            c < 0 or
            r == rows or
            c == cols or
            visited[r][c] or
            grid[r][c] == "0"
        ): return
        
        visited[r][c] = True
        # going-up
        self.dfs(grid, visited, r-1, c, rows, cols)
        # going-down
        self.dfs(grid, visited, r+1, c, rows, cols)
        # going-right
        self.dfs(grid, visited, r, c+1, rows, cols)
        # going-left
        self.dfs(grid, visited, r, c-1, rows, cols)
        

    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count_island = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    count_island += 1
                    self.dfs(grid, visited, r, c, rows, cols)
        return count_island
        