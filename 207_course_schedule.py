class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courseGraph = {}
        for pre in prerequisites:
            if pre[1] in courseGraph:
                courseGraph[pre[1]].append(pre[0])  
            else:
                courseGraph[pre[1]] = [pre[0]]  
                
        visited = set()  
        
        def courseSchedule(course: int) -> bool:
            
            if course in visited:
                return False  
                
            
            if course not in courseGraph or courseGraph[course] is None:
                return True  
                
            visited.add(course)  
            
            
            for pre in courseGraph[course]:
                if not courseSchedule(pre):
                    return False  
                    
            visited.remove(course)  
            courseGraph[course] = None  
            return True  

        
        for currentCourse in range(numCourses):
            if not courseSchedule(currentCourse):
                return False  
                
        return True  
