class Solution:
    def dfs(self, board, visited, rows, cols, r, c, target, index):
        if index == len(target):
            return True
        
        if (
            r < 0 or
            c < 0 or
            r == rows or
            c == cols or
            target[index] != board[r][c] or
            visited[r][c]
        ): return False

        index += 1
        visited[r][c] = True

        res = (
            # going up
            self.dfs(board, visited, rows, cols, r-1, c, target, index) or
            # going down
            self.dfs(board, visited, rows, cols, r + 1, c, target, index) or
            # going right
            self.dfs(board, visited, rows, cols, r, c + 1, target, index) or
            # going left
            self.dfs(board, visited, rows, cols, r, c - 1, target, index)
        )

        visited[r][c] = False
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if (
                    board[r][c] == word[0] and
                    self.dfs(board, visited, rows, cols, r, c, word, 0)
                ): return True

        return False

        