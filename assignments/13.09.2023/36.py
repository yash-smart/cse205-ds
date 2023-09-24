class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns
        for i in range(9):
            row_check = []
            column_check = []
            for j in range(9):
                value = board[i][j]
                if value != '.':
                    if value in row_check:
                        return False
                    else:
                        row_check.append(value)
                value = board[j][i]
                if value != '.':
                    if value in column_check:
                        return False
                    else:
                        column_check.append(value)
        # Check boxes
        for i in range(3):
            for j in range(3):
                box_check = []
                for a in range(3):
                    for b in range(3):
                        value = board[i*3+a][j*3+b]
                        if value != '.':
                            if value in box_check:
                                return False
                            else:
                                box_check.append(value)
        return True
    
