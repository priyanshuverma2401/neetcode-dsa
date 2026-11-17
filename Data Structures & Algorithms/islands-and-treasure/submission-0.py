class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()

        def addQ(r, c, dist):
            if (
                r < 0 or
                r == ROWS or
                c < 0 or
                c == COLS or
                grid[r][c] == -1 or
                (r, c) in visited
            ): return
            grid[r][c] = dist+1
            queue.append((r, c, dist+1))
            visited.add((r, c))
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            r, c, dist = queue.popleft()
            addQ(r+1, c, dist)
            addQ(r-1, c, dist)
            addQ(r, c-1, dist)
            addQ(r, c+1, dist)

        



        
        