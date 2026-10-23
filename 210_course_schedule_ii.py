class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        WHITE, GRAY, BLACK = 1, 2, 3
        
        isPossible = True
        color = {i: WHITE for i in range(numCourses)}
        adjList = {i: [] for i in range(numCourses)}
        topologicalOrder = []
        
        for dest, src in prerequisites:
            adjList[src].append(dest)
            
        def dfs(node: int):
            nonlocal isPossible
            if not isPossible:
                return
            
            color[node] = GRAY
            
            for neighbor in adjList.get(node, []):
                if color[neighbor] == WHITE:
                    dfs(neighbor)
                elif color[neighbor] == GRAY:
                    isPossible = False
                    
            color[node] = BLACK
            topologicalOrder.append(node)

        for i in range(numCourses):
            if color[i] == WHITE:
                dfs(i)
                
        
        if isPossible:
            return topologicalOrder[::-1]  
        else:
            return []  
