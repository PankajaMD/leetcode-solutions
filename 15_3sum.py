class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final = []
        num = sorted(nums)
        for a in range(len(num)):
            if a > 0 and num[a] == num[a-1]:
                continue
            i = num[a]
            sum = 0 - i
            l = a+1
            r = len(num) - 1
            while l < r:
                if num[l] + num[r] > sum:
                    r -= 1
                elif num[l] + num[r] < sum:
                    l += 1
                else:
                    final.append([i,num[l],num[r]])
                    l += 1
                    r -= 1
                    while l < r and num[l] == num[l-1]:
                        l += 1
                    while l < r and num[r] == num[r+1]:
                        r -= 1
        return final
        
