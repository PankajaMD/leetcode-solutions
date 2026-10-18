class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True
            
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                board[row][col] != word[index]):
                return False
            
            
            temp = board[row][col]
            board[row][col] = '#'
            
            
            rowdir = [0, 1, 0, -1]
            coldir = [1, 0, -1, 0]
            
            ret = False
            for d in range(4):
                if backtrack(row + rowdir[d], col + coldir[d], index + 1):
                    ret = True
                    break
            
            board[row][col] = temp
            return ret

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
                    
        return False
