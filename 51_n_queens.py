class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        
        def isValid(row: int, col: int) -> bool:
            
            for i in range(col):
                if board[row][i] == 'Q':
                    return False
            
            
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            
            i, j = row, col
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1
                
            return True  

        def backtrack(col: int):
            if col == n:
                result.append(["".join(row) for row in board])
                return
            
            for i in range(n):
                if isValid(i, col):
                    board[i][col] = 'Q'
                    backtrack(col + 1)
                    board[i][col] = '.'

        backtrack(0)
        return result
