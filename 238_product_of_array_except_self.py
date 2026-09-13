class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        ans = [1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = pre
            else:
                ans[i] = pre * nums[i-1]
            pre = ans[i]
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= post
            post *= nums[j]      
        
        return ans
