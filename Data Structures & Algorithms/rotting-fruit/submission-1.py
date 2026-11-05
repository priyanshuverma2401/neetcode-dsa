class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        rows_count, cols_count = len(grid), len(grid[0])
        q = collections.deque()

        for row in range(rows_count):
            for col in range(cols_count):
                if grid[row][col] == 1: fresh+=1
                elif grid[row][col] == 2: q.append((row, col))
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                # checking upper
                if r-1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q.append((r-1, c))
                    fresh-=1
                # checking down
                if r+1 < rows_count and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    q.append((r+1, c))
                    fresh-=1
                # checking left
                if c-1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    q.append((r, c-1))
                    fresh-=1
                # checking right
                if c + 1 < cols_count and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    q.append((r, c+1))
                    fresh-=1
            time+=1
        return -1 if fresh > 0 else time




        
        