class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        length = float('inf')
        unique = len(set(t))
        start = 0
        targetMap = [0] * 128
        windowMap = [0] * 128
        
        for i in range(len(t)):
            targetMap[ord(t[i])] += 1
        
        l = 0
        r = 0
        while r < len(s):
            windowMap[ord(s[r])] += 1
            create = self.count_matches(windowMap, targetMap)
            while create == unique:
                if (r - l + 1) < length:
                    length = r - l + 1
                    start = l
                windowMap[ord(s[l])] -= 1
                create = self.count_matches(windowMap, targetMap)
                l += 1
            r += 1
        
        return "" if length == float('inf') else s[start:start+length]
    
    def count_matches(self, windowMap, targetMap):
        count = 0
        for i in range(128):
            if targetMap[i] > 0 and windowMap[i] >= targetMap[i]:
                count += 1
        return count
