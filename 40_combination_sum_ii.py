class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()  
        
        def backtrack(current: list[int], target: int, start: int):
            if target == 0:
                result.append(list(current))  
                return
            
            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  
                
                
                if target - candidates[i] < 0:
                    break  
                
                current.append(candidates[i])  
                backtrack(current, target - candidates[i], i + 1)  
                current.pop()  
                
        backtrack([], target, 0)
        return result
