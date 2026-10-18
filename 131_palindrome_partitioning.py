class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        
        def backtrack(current: list[str], start: int):
            if start == len(s):
                result.append(list(current))  
                return
            
            for end in range(start, len(s)):
                if self.isPalindrome(s, start, end):
                    current.append(s[start:end + 1])  
                    backtrack(current, end + 1)  
                    current.pop()  
                    
        backtrack([], 0)
        return result

    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
