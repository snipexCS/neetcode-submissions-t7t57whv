class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for rows in range(9):
            for cols in range(9):
                if board[rows][cols] == '.':
                    continue
                if board[rows][cols] in row[rows] or  board[rows][cols] in col[cols] or board[rows][cols] in square[(rows//3,cols//3)]:
                    return False
                

                row[rows].add(board[rows][cols])
                col[cols].add(board[rows][cols])
                square[(rows//3,cols//3)].add(board[rows][cols])
        
        return True

        
        