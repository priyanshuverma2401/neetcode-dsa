class Solution:
    def dfs(self, row, col, grid):
        ROWS, COLS = len(grid), len(grid[0])
        stack = []
        stack.append((row, col))
        self.visited.add((row, col))

        while stack:
            r, c = stack.pop()
            # going DOWN
            if r+1 < ROWS and grid[r+1][c] == "1" and (r+1, c) not in self.visited:
                stack.append((r+1, c))
                self.visited.add((r+1, c))
            # going UP
            if r-1 >= 0 and grid[r-1][c] == "1" and (r-1, c) not in self.visited:
                stack.append((r-1, c))
                self.visited.add((r-1, c))
            # going LEFT
            if c-1 >= 0 and grid[r][c-1] == "1" and (r, c-1) not in self.visited:
                stack.append((r, c-1))
                self.visited.add((r, c-1))
            # going RIGHT
            if c+1 < COLS and grid[r][c+1] == "1" and (r, c+1) not in self.visited:
                stack.append((r, c+1))
                self.visited.add((r, c+1))


    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        self.visited = set()
        island = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    self.dfs(r, c, grid)
                    island+=1
        return island
        