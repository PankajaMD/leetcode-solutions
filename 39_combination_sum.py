class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(target: int, combination: list[int], start: int):
            if target == 0:
                res.append(list(combination))  # Add a copy of the combination when target is met[cite: 13]
                return
            elif target < 0:
                return  # Stop recursion if target becomes negative[cite: 14]
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])  # Choose the candidate[cite: 14]
                backtrack(target - candidates[i], combination, i)  # Recurse with the same index (unlimited choices)[cite: 14]
                combination.pop()  # Backtrack by removing the last element[cite: 14]
                
        backtrack(target, [], 0)
        return res
