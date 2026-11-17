class Solution:
    def bfs(self, row, col, grid):
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        q.append((row, col))
        self.visited.add((row, col))

        while q:
            r, c = q.popleft()
            # going Up
            if r-1 >= 0 and grid[r-1][c] == "1" and (r-1, c) not in self.visited:
                q.append((r-1, c))
                self.visited.add((r-1, c))
            # going Down
            if r+1 < ROWS and grid[r+1][c] == "1" and (r+1, c) not in self.visited:
                q.append((r+1, c))
                self.visited.add((r+1, c))
            # going Left
            if c-1 >= 0 and grid[r][c-1] == "1" and (r, c-1) not in self.visited:
                q.append((r, c-1))
                self.visited.add((r, c-1))
            # going Right
            if c+1 < COLS and grid[r][c+1] == "1" and (r, c+1) not in self.visited:
                q.append((r, c+1))
                self.visited.add((r, c+1))


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        self.visited = set()

        ROWS, COLS = len(grid), len(grid[0])
        island = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    self.bfs(r, c, grid)
                    island+=1
        
        return island






        