class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        ROWS = len(matrix)
        COLS = len(matrix[0])
        right = ROWS*COLS-1

        while left<=right:
            m = (left + right) // 2
            row = m // COLS
            col = m - (row * COLS)
            if matrix[row][col] == target:
                return True
            elif  matrix[row][col] > target:
                right = m - 1
            elif  matrix[row][col] < target:
                left = m + 1
        
        return False


        