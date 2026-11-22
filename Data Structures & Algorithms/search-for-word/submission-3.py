class Solution:
    def backtrack(self, board, row, col, word, ROWS, COLS, index, word_arr):
        if "".join(x for x in word_arr) == word:
            return True
        elif row == ROWS or col == COLS or row < 0 or col < 0 or index == len(word) or board[row][col] != word[index]:
            return False
        

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        word_arr.append(board[row][col])
        self.visited.add((row, col))
        for dr, dc in directions:
            drow, dcol = row + dr, col + dc
            if (drow, dcol) not in self.visited and self.backtrack(board, drow, dcol, word, ROWS, COLS, index+1, word_arr):
                return True
        if (row, col) in self.visited: self.visited.remove((row, col))
        if word_arr: word_arr.pop()
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        self.visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and self.backtrack(board, r, c, word, ROWS, COLS, 0, []):
                    return True
        return False

        