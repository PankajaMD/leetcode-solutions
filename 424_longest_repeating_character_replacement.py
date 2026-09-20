class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurance = [0] * 26
        left = 0
        ans = 0
        maxOccurance = 0
        
        for right in range(len(s)):
            occurance[ord(s[right]) - ord('A')] += 1
            maxOccurance = max(maxOccurance, occurance[ord(s[right]) - ord('A')])
            
            if right - left + 1 - maxOccurance > k:
                occurance[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
