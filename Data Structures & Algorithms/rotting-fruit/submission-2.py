class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        fresh, rotten, time = 0, 0, 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: fresh+=1
                if grid[r][c] == 2: 
                    rotten+=1
                    queue.append((r, c))
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    drow, dcol = r + dr, c + dc
                    if(
                        drow >= 0 and 
                        drow < ROWS and
                        dcol >= 0 and 
                        dcol < COLS and
                        grid[drow][dcol] == 1
                    ):
                        grid[drow][dcol] = 2
                        fresh-=1
                        queue.append((drow, dcol))
            time+=1

        return time if fresh == 0 else -1

            
            



        