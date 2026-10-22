class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0  
        
        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0  
            
            grid[i][j] = 0  
            area = 1  
            
            area += dfs(i + 1, j)  
            area += dfs(i - 1, j)  
            area += dfs(i, j + 1)  
            area += dfs(i, j - 1)  
            
            return area  

        for i in range(rows):  
            for j in range(cols):  
                if grid[i][j] == 1:  
                    area = dfs(i, j)  
                    maxArea = max(maxArea, area)  
                    
        return maxArea  
