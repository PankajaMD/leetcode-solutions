class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        used = [False] * len(nums)  # Tracks whether a number has been used[cite: 15]
        
        def backtrack(current: list[int]):
            if len(current) == len(nums):
                result.append(list(current))  # Add a copy of the current permutation[cite: 15]
                return
            
            for i in range(len(nums)):
                if not used[i]:  # If the number is not used[cite: 15]
                    current.append(nums[i])  # Choose the number[cite: 15]
                    used[i] = True  # Mark it as used[cite: 15]
                    backtrack(current)  # Recurse to build the rest of the permutation[cite: 15]
                    used[i] = False  # Backtrack: unmark as used[cite: 15]
                    current.pop()  # Backtrack: remove the number[cite: 15]
                    
        backtrack([])
        return result
