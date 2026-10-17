class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def generateSubsets(index: int, current: list[int]):
            result.append(list(current))  
            for i in range(index, len(nums)):
                current.append(nums[i])  
                generateSubsets(i + 1, current)  
                current.pop()  
                
        generateSubsets(0, [])
        return result
