class Solution:
    def findArea(self, row, col, grid):
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        q.append((row, col))
        self.visited.add((row, col))
        area = 0

        while q:
            r, c = q.popleft()
            area+=1
            # Going LEFT
            if c-1 >= 0 and grid[r][c-1] == 1 and (r, c-1) not in self.visited:
                q.append((r, c-1))
                self.visited.add((r, c-1))
            # Going RIGHT
            if c+1 < COLS and grid[r][c+1] == 1 and (r, c+1) not in self.visited:
                q.append((r, c+1))
                self.visited.add((r, c+1))
            # Going UP
            if r-1 >= 0 and grid[r-1][c] == 1 and (r-1, c) not in self.visited:
                q.append((r-1, c))
                self.visited.add((r-1, c))
            # Goinf Down
            if r+1 < ROWS and grid[r+1][c] == 1 and (r+1, c) not in self.visited:
                q.append((r+1, c))
                self.visited.add((r+1, c))
        return area



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        self.visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in self.visited:
                    # print(self.findArea(r, c, grid))
                    maxArea = max(maxArea, self.findArea(r, c, grid))
        return maxArea

        