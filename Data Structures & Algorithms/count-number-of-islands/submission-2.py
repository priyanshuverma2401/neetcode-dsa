class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows_count, cols_count = len(grid), len(grid[0])
        visited = [[False for _ in range(cols_count)] for _ in range(rows_count)]

        def dfs(r, c):
            if grid[r][c] != "1" or visited[r][c]: return

            visited[r][c] = True
            # going down
            if r + 1 < rows_count:
                dfs(r+1, c)
            # going up
            if r - 1 >= 0:
                dfs(r-1, c)
            # going left
            if c-1 >= 0:
                dfs(r, c-1)
            # going right
            if c + 1 < cols_count:
                dfs(r, c+1)
            

        for r in range(rows_count):
            for c in range(cols_count):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    islands+=1
        return islands



        