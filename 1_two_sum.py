class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            dig = target - nums[i]
            if dig in map:
                return [map[dig], i]
            map[nums[i]] = i
