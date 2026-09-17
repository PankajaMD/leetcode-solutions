class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        value = 0
        while l < r:
            num = min(height[l], height[r])
            area = num * (r - l)
            value = max(value, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return value
