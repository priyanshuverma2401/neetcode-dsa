class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) #O(N^2)
        cols = defaultdict(set) #O(N^2)
        squares = defaultdict(set) #(N^2)

        for row in range(9): #O(N)
            for col in range(9): #O(N)
                if board[row][col] == ".":
                    continue
                if (
                    board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row // 3, col // 3)]
                ): return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])
        return True

# Time Complexity: O(N^2)
# Space complexity: O(N^2)
        