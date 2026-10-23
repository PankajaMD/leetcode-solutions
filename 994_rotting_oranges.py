class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1  
            
        m, n = len(grid), len(grid[0])  
        freshCount = 0  
        rottenQueue = deque()  
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCount += 1  
                elif grid[i][j] == 2:
                    rottenQueue.append((i, j))  
                    
        if freshCount == 0:
            return 0  
            
        minutes = 0  
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  
        
        while rottenQueue:
            size = len(rottenQueue)  
            for _ in range(size):  
                r, c = rottenQueue.popleft()  
                for dr, dc in directions:  
                    x, y = r + dr, c + dc  
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:  
                        grid[x][y] = 2  
                        freshCount -= 1  
                        rottenQueue.append((x, y))  
            minutes += 1  
            
        return minutes - 1 if freshCount == 0 else -1
