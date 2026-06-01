class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        squares = {}

        for i in range(9):
            row = {}
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in row:
                    return False
                if j not in cols:
                    cols[j] = {}
                if val in cols[j]:
                    return False
                square_id = j//3 + (i//3)*3
                if square_id not in squares:
                    squares[square_id] = {}
                if board[i][j] in squares[square_id]:
                    return False
                cols[j][val] = 1
                squares[square_id][val] = 1
                row[val] = 1
        
        return True
 