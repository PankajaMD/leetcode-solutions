class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []  
            
        row, col = len(heights), len(heights[0])  
        pacificReachable = [[False for _ in range(col)] for _ in range(row)]  
        atlanticReachable = [[False for _ in range(col)] for _ in range(row)]  
        
        def dfs(r: int, c: int, reachable: list[list[bool]]):
            reachable[r][c] = True  
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]  
            for dr, dc in directions:
                newRow, newCol = r + dr, c + dc  
                if 0 <= newRow < row and 0 <= newCol < col:  
                    if not reachable[newRow][newCol] and heights[newRow][newCol] >= heights[r][c]:  
                        dfs(newRow, newCol, reachable)  
                        
        
        for i in range(row):
            dfs(i, 0, pacificReachable)  
            dfs(i, col - 1, atlanticReachable)  
            
        
        for i in range(col):
            dfs(0, i, pacificReachable)  
            dfs(row - 1, i, atlanticReachable)  
            
        result = []
        for i in range(row):
            for j in range(col):
                if pacificReachable[i][j] and atlanticReachable[i][j]:
                    result.append([i, j])
                    
        return result
