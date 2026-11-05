class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_of_island = 0
        rows_count, col_count = len(grid), len(grid[0])
        visited = [[0 for _ in range(col_count)] for _ in range (rows_count)]

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visited[row][col] = 1

            while q:
                r, c = q.popleft()
                # going up
                if r - 1 >= 0 and grid[r-1][c] == "1" and not visited[r-1][c]:
                    q.append((r-1, c))
                    visited[r-1][c] = 1
                # going down
                if r + 1 < rows_count and grid[r+1][c] == "1" and not visited[r+1][c]:
                    q.append((r+1, c))
                    visited[r+1][c] = 1
                # going left
                if c-1 >= 0 and grid[r][c-1] == "1" and not visited[r][c-1]:
                    q.append((r, c-1))
                    visited[r][c-1] = 1
                # going right
                if c + 1 < col_count and grid[r][c+1] == "1" and not visited[r][c+1]:
                    q.append((r, c+1))
                    visited[r][c+1] = 1


        for row in range(rows_count):
            for col in range(col_count):
                if grid[row][col] == "1" and not visited[row][col]:
                    bfs(row, col)
                    no_of_island += 1
        return no_of_island
            
        