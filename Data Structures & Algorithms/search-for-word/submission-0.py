class Solution:

    def dfs(self, board, visited, r, c, rows, cols, index, target):
        if index == len(target): return True

        if  (r < 0 or c < 0 or r == rows 
            or c == cols or board[r][c] != target[index] 
            or visited[r][c]): 
            return False

        index += 1
        visited[r][c] = True

        res = (
        # going up
        self.dfs(board, visited, r-1, c, rows, cols, index, target)
        or
        # going down
        self.dfs(board, visited, r + 1, c, rows, cols, index, target)
        or
        # going right
        self.dfs(board, visited, r, c+1, rows, cols, index, target)
        or
        # going left
        self.dfs(board, visited, r, c-1, rows, cols, index, target)
        )

        visited[r][c] = False
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if self.dfs(board, visited, r, c, rows, cols, 0, word): return True

        return False
                
        