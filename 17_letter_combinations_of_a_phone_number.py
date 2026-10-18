class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        digitToLetters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        combinations = []
        
        def backtrack(currentCombination: str, index: int):
            if index == len(digits):
                combinations.append(currentCombination)  
                return
            
            letters = digitToLetters[int(digits[index])]  
            for letter in letters:
                backtrack(currentCombination + letter, index + 1)  
                
        backtrack("", 0)  
        return combinations
