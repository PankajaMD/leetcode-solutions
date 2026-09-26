class Solution:
    def search(self, nums: list[int], target: int) -> int:
        high = len(nums) - 1
        low = 0 
        mid = 0
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1




