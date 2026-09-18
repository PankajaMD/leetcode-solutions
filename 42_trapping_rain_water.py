class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        
        total = 0
        leftMax = height[0]
        rightMax = height[right]
        
        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                if leftMax - height[left] > 0:
                    total += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                if rightMax - height[right] > 0:
                    total += rightMax - height[right]
                right -= 1
        
        return total
