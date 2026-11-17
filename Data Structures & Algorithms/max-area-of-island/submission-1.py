class Solution:
    def dfs(self, row, col, grid):
        if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1 or (row, col) in self.visited: 
            return 0
        
        area = 1
        self.visited.add((row, col))

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in direction:
            area += self.dfs(row + dr, col + dc, grid)
        
        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.visited = set()
        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in self.visited:
                    maxArea = max(maxArea, self.dfs(r, c, grid))
        return maxArea
