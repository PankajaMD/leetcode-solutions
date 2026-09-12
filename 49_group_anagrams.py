class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in strs:
            nums = [0]*26
            for j in range(len(i)):
                nums[ord(i[j]) - ord('a')] += 1
            
            key = tuple(nums)
            if key not in map:
                map[key] = []
            map[key].append(i)
        
        result = [values for values in map.values()]
        return result
