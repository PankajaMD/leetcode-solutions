class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or len(nums) == 0 or k <= 0:
            return []
        
        n = len(nums)
        result = [0] * (n - k + 1)
        dq = deque()   
        
        for i in range(n):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            if i >= k - 1:
                result[i - k + 1] = nums[dq[0]]
        
        return result
