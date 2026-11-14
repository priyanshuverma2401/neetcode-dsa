class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        up, bottom = 0, ROWS-1
        target_row = -1

        while up <= bottom:
            mid = (up + bottom) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][COLS-1]:
                target_row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid-1
            else:
                up = mid+1
        
        if target_row == -1: return False
        
        left, right = 0, COLS-1

        while left <= right:
            mid = (left + right) // 2
            if matrix[target_row][mid] == target: return True
            elif matrix[target_row][mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        return False

        